from django.db import models
from django.contrib.auth.models import User, Group
from django.db import connection
from django.core.mail import EmailMultiAlternatives
from django.template import Context, Template
from django.conf import settings
from django.contrib.sites.models import Site

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^emailer\.fields\.DictionaryField"])

from emailer.html2text import html2text
from emailer.fields import DictionaryField

import uuid, json, datetime

def make_uuid():
    return str(uuid.uuid4())

class DefaultModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False)
    
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_changed = models.DateTimeField('date changed', auto_now=True)

    class Meta:
        abstract = True
  
class EmailTemplate(DefaultModel):
    name = models.CharField(blank=False, max_length=40)
    description = models.TextField(blank=True)
    html = models.TextField(blank=False)
    
    def __unicode__(self):
        return str(self.name)
    
    @models.permalink
    def get_absolute_url(self):
        return ('emailer-template', (), {'template_id': self.id})

class EmailListManager(models.Manager):

    def get_query_set(self):
        return super(EmailListManager, self).get_query_set().exclude(is_oneoff=True)

class EmailList(DefaultModel):
    LISTTYPE_SITEUSERS_USERDEFINED = 0
    LISTTYPE_QUERY_CUSTOM_SQL = 1
    LISTTYPE_RAW_EMAILS = 2
    LISTTYPE_RAW_JSON = 3
    LISTTYPE_SITEGROUPS = 4
    
    EMAIL_LIST_TYPE_CHOICES = (
                         (LISTTYPE_SITEUSERS_USERDEFINED,'Site Users - User Defined'),
                         (LISTTYPE_QUERY_CUSTOM_SQL, 'Custom SQL Query'),
                         (LISTTYPE_RAW_EMAILS, 'Raw Emails'),
                         (LISTTYPE_RAW_EMAILS, 'Raw JSON'),
                         (LISTTYPE_SITEGROUPS, 'Site Groups'),
                         )
    
    class RawEmail():
        def __init__(self, email):
            self.email = email
    
    name = models.CharField(blank=False, unique=True, max_length=40)
    type = models.IntegerField(
                               blank=False,
                               choices=EMAIL_LIST_TYPE_CHOICES, 
                               default=LISTTYPE_SITEUSERS_USERDEFINED
                               )
    data_raw_emails = models.TextField(blank=True)
    data_site_users = models.ManyToManyField(User, blank=True)
    data_query_sql = models.TextField(blank=True)
    data_raw_json = models.TextField(blank=True)
    data_site_groups = models.ManyToManyField(Group, blank=True)
    
    is_oneoff = models.BooleanField(default=False)

    objects = EmailListManager()

    class Meta:
        ordering = ['name']

    def _is_valid_field(self, field):
        return not field == 'id' and not field.startswith('_')
    
    def _get_user_objs(self, users):
        try:
            #try to include profile fields on User object            
            for u in users:
                for field,value in u.get_profile().__dict__.iteritems():
                    if self._is_valid_field(field):
                        setattr(u, field, value)
        except:
            #eat this if there is no profile defined in settings.py
            pass
        return users
    
    def get_objects(self):
        
        if self.type in (EmailList.LISTTYPE_SITEUSERS_USERDEFINED,):
            users = self._get_user_objs(self.data_site_users.all())
            return users
        
        elif self.type == EmailList.LISTTYPE_SITEGROUPS:
            users = []
            groups = self.data_site_groups.all()
            
            for group in groups:
                users += self._get_user_objs(group.user_set.all())
                
            return users
        
#        elif self.type in (EmailList.LISTTYPE_QUERY_CUSTOM_SQL,):
#            cursor = connection.cursor()
#            cursor.execute(self.data_query_sql)
#            rows = cursor.fetchall()
#            objs = []
#            for row in rows:#not good
#                objs.append(EmailList.RawEmail(row[0]))
#            return objs
        
        elif self.type in (EmailList.LISTTYPE_RAW_EMAILS,):
            return [EmailList.RawEmail(email.strip()) for email in self.data_raw_emails.split(',')]
        
#        elif self.type in (EmailList.LISTTYPE_RAW_JSON,):
#            json.loads(self.data_raw_json)
#            return []
        
        else:
            raise NotImplementedError()
    
    def preview_emails(self):
        try:
            objs = self.get_objects()[:3]
        except:
            objs = self.get_objects()
        preview = u', '.join([obj.email for obj in objs if obj.email])
        return preview if preview else u'(No emails found)'
    preview_emails.short_description = 'Preview Emails'
    preview_emails.allow_tags = True
    
    def merge_fields(self):
        try:
            obj = self.get_objects()[0]
        except:
            obj = EmailList.RawEmail("")
            
        return obj.__dict__.keys()
    merge_fields.short_description = 'Merge Fields'
    merge_fields.allow_tags = True
    
    def save(self, *args, **kwargs):
        if self.is_oneoff and not self.name.startswith('_'):
            self.name = '_'+self.name
        models.Model.save(self,*args, **kwargs)        
         
    def __unicode__(self):
        return str(self.name)

class EmailBlast(DefaultModel):    
    name = models.CharField(blank=False, unique=False, max_length=50)
    lists = models.ManyToManyField(EmailList)

    is_prepared = models.BooleanField(default=False)
    send_after = models.DateTimeField(blank=False,
        help_text='This is the date the email is going to be sent after. The email also must be prepared before it is sent.')
    from_address = models.EmailField(blank=False)
    subject = models.CharField(blank=False, max_length=40)
    
    html = models.TextField(blank=False)

    class Meta:
        ordering = ['-date_created']

    def __unicode__(self):
        return str(self.name)
    
    def _prepare_for_send(self):
        if not self.is_prepared:
            for list in self.lists.all():
                for obj in list.get_objects():
                    email = Email()
                    email.email_blast = self
                    email.to_address = obj.email
                    email.merge_data = obj.__dict__
                    email.status = Email.STATUS_PREPARED
                    email.save()
            self.is_prepared = True
            self.save()
                    
    def send(self, just_prepare=False):
        '''
        Sends an email for all objects in the assigned lists.
        '''
        if not self.is_prepared:
            self._prepare_for_send()

        if not just_prepare or not datetime.datetime.now() > self.send_after:
            for email in Email.objects.filter(email_blast=self):
                email.send()

    def lists_str(self):
        lists = [list.name for list in self.lists.all()]
        return u', '.join(lists) if lists else 'One Off List'
    lists_str.short_description = 'Lists'
    lists_str.allow_tags = True

def _apply_merge_data(html, merge_data):
    t = Template(html)
    c = Context(merge_data)
    return t.render(c)

class IncorrectEmailStatus(Exception):
    def __init__(self):
        Exception.__init__(self)
                  
class EmailManager(models.Manager):
    
    def email_from_tracking(self, id):
        return self.get(id=id)

class Email(DefaultModel):
    STATUS_PREPARED = 0
    STATUS_SENT = 1
    STATUS_ERROR = 2
    
    STATUS_CHOICES = (
                     (STATUS_PREPARED, 'Prepared'),
                     (STATUS_SENT, 'Sent'),
                     (STATUS_ERROR, 'Error'),
                     )
    
    email_blast = models.ForeignKey(EmailBlast, blank=False)
    to_address = models.EmailField(blank=False)
    merge_data = DictionaryField(editable=False, blank=True)
    
    status = models.IntegerField(blank=False, choices=STATUS_CHOICES, default=STATUS_PREPARED, editable=False)
    status_message = models.TextField(blank=True, editable=False)
    opened = models.BooleanField(default=False, editable=False)
    
    objects = EmailManager()
    
    def _subject(self): return self.email_blast.subject
    subject = property(_subject)
    
    def _from_address(self): return self.email_blast.from_address
    from_address = property(_from_address)
    
    def _html(self): return self.email_blast.html
    html = property(_html)
    
    class Meta:
        ordering = ['-date_created']
    
    @models.permalink
    def get_tracking_png_url(self):
        return ('emailer-tracking_png', (), {'tracking_id': self.id})
    
    def _append_tracking_image(self, html):    
        tracking_url = 'http://%s%s' % (Site.objects.get_current().domain, self.get_tracking_png_url())
        
        html = html + r'<img src="%s" alt="tracking url" id="trackingurl" />' %str(tracking_url)
        return html
    
    def _add_tracking_info(self, html):
        tracking_html = self._append_tracking_image(html)
        
        return tracking_html

    def _convert_relative_urls(self, html):
        return html
    
    def _prepare_html(self):
        html = _apply_merge_data(self.html, self.merge_data)
        html = self._convert_relative_urls(html)
        
        return html
    
    def _build_message(self):
        blast = self.email_blast
        
        subject = blast.subject
        from_email = blast.from_address
        to = self.to_address
        
        fixed_html = self._prepare_html()
        
        text_content = html2text(fixed_html)
        html_content = self._add_tracking_info(fixed_html)
        
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
    
        return msg
    
    def send(self):
        '''
        Actually send the email using django email. If the associated blasts
        send datetime is not after the current datetime, the email will not
        be sent. This will be a silent failure. You should not call this
        method directly, it should be called by a blast or a processor.
        '''
        if datetime.datetime.now() > self.email_blast.send_after:
            if self.status != Email.STATUS_PREPARED:
                raise IncorrectEmailStatus("Email is not in status of prepared, something bad must have happened!")

            message = self._build_message()

            try:
                message.send()
                self.status = Email.STATUS_SENT
            except Exception, e:
                self.status = Email.STATUS_ERROR
                self.status_message = str(e)

            self.save()
