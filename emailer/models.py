from django.db import models
    
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
    name = models.CharField(blank=False, max_length=40)
    description = models.TextField(blank=True)
    html = models.TextField(blank=False)
    
    def __unicode__(self):
        return str(self.name)
    
    @models.permalink
    def get_absolute_url(self):
        return ('emailer-template', (), {'template_id': self.id})
    
class EmailList(DefaultModel):
    LISTTYPE_SITEUSERS_USERDEFINED = 0
    
    EMAIL_LIST_TYPE_CHOICES = (
                         (LISTTYPE_SITEUSERS_USERDEFINED,'Site Users - User Defined'),
                         )
    
    name = models.CharField(blank=False, unique=True, max_length=40)
    type = models.IntegerField(
                               blank=False,
                               choices=EMAIL_LIST_TYPE_CHOICES, 
                               default=LISTTYPE_SITEUSERS_USERDEFINED
                               )
        
    def get_users(self):
        
        if self.type in (EmailList.LISTTYPE_SITEUSERS_USERDEFINED):
            return []
        else:
            raise NotImplementedError()
       
    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return str(self.name)

class EmailBlast(DefaultModel):
    BLASTTYPE_ONEOFF = 0
    
    EMAIL_BLAST_LIST_CHOICES = (
                         (BLASTTYPE_ONEOFF,'One off email'),
                         )
    
    name = models.CharField(blank=False, unique=True, max_length=40)
    type = models.IntegerField(
                               blank=True,
                               choices=EMAIL_BLAST_LIST_CHOICES, 
                               default=BLASTTYPE_ONEOFF
                               )
    send_after = models.DateTimeField(blank=False)
    from_address = models.EmailField(blank=False)
    subject = models.CharField(blank=False, max_length=40)
        
    html = models.TextField(blank=False)
        
    class Meta:
        ordering = ['date_created']

    def __unicode__(self):
        return str(self.name)
        
class EmailManager(models.Manager):
    
    def email_from_tracking(self, id):
        return self.get(id=id)
    
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
    merge_data = models.TextField(editable=False)
    
    status = models.IntegerField(blank=False, choices=STATUS_CHOCES, default=STATUS_PREPARED, editable=False)
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
        ordering = ['date_created']
    
    @models.permalink
    def get_tracking_png_url(self):
        return ('emailer-tracking_png', (), {'tracking_id': self.id})
    