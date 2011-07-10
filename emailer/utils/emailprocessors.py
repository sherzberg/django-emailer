

from django.conf import settings
import datetime

from emailer.models import Email

class IEmailProcessor():
    
    def prepare_emails(self):
        raise NotImplementedError
    
    def process_emails(self):
        raise NotImplementedError
    
class SimpleProcessor(IEmailProcessor):
    
    def prepare_emails(self, blast=None):
        if blast:
            self.emails_to_process = Email.objects.filter(status=Email.STATUS_PREPARED, email_blast=blast)
        else:
            self.emails_to_process = Email.objects.filter(status=Email.STATUS_PREPARED)
    
        return len(self.emails_to_process)
    
    def process_emails(self):
        for email in self.emails_to_process:     
            status = email.send()
            
        return len(self.emails_to_process)
    