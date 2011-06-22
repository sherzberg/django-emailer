from django.db import models
try:
    from tinymce.models import HTMLField
except:
    from django.db.models import TextField as HtmlField
    
import uuid, datetime

def make_uuid():
    return str(uuid.uuid4())

class DefaultModel(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=make_uuid, editable=False)
    
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_changed = models.DateTimeField('date changed', auto_now=True)

    class Meta:
        abstract = True
  
class EmailTemplate(DefaultModel):
    name = models.CharField(blank=False, unique=True, max_length=40)
    description = models.TextField(blank=True)
    html = HTMLField(blank=False)
    
    def __unicode__(self):
        return str(self.name)
    
class EmailList(DefaultModel):
    TYPE_SITEUSERS_USERDEFINED = 0
    
    EMAIL_LIST_CHOICES = (
                         (TYPE_SITEUSERS_USERDEFINED,'Site Users - User Defined'),
                         )
    
    name = models.CharField(blank=False, unique=True, max_length=40)
    type = models.IntegerField(
                               blank=False,
                               choices=EMAIL_LIST_CHOICES, 
                               default=TYPE_SITEUSERS_USERDEFINED
                               )
    
    def get_users(self):
        
        if self.type in (EmailList.TYPE_SITEUSERS_USERDEFINED):
            return []
        else:
            raise NotImplementedError()
       
    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return str(self.name)
    
class EmailBlast(DefaultModel):
    name = models.CharField(blank=False, unique=True, max_length=40)
    send_after = models.DateTimeField(blank=False)
    list = models.ForeignKey(EmailList, blank=True)
    
    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return str(self.name)
        
class EmailManager(models.Manager):
    
    def email_from_tracking(self, id):
        return self.get(uuid=id)
    
class Email(DefaultModel):
    STATUS_PREPARED = 0
    STATUS_SENT = 1
    STATUS_ERRORED = 2
    
    STATUS_CHOCES = (
                     (STATUS_PREPARED, 'Prepared'),
                     (STATUS_SENT, 'Sent'),
                     (STATUS_ERRORED, 'Errored'),
                     )
    
    email_blast = models.ForeignKey(EmailBlast, blank=False)
    to_address = models.EmailField(blank=False)
    from_address = models.EmailField(blank=False)
    subject = models.CharField(blank=False, max_length=40)
    
    status = models.IntegerField(blank=False, choices=STATUS_CHOCES, default=STATUS_PREPARED, editable=False)
    status_message = models.TextField(blank=True, editable=False)
    
    content_html = HTMLField(blank=False)
    merge_data = models.TextField(editable=False)
    
    opened = models.BooleanField(default=False, editable=False)
    
    objects = EmailManager()
    
    class Meta:
        ordering = ['date_created']
    
    @models.permalink
    def get_tracking_png_url(self):
        return ('emailer-tracking_png', (), {'tracking_id': self.uuid})
    