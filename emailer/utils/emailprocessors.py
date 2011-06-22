

from django.conf import settings
import datetime

from emailer.models import Email
from emailer.utils import send_email


class IEmailProcessor():
    
    def prepare_emails(self):
        raise NotImplementedError
    
    def process_emails(self):
        raise NotImplementedError
    
class SimpleProcessor(IEmailProcessor):
    
    def prepare_emails(self):
        self.emails_to_process = Email.objects.filter(status=Email.STATUS_PREPARED)
    
        return len(self.emails_to_process)
    
    def process_emails(self):
        for email in self.emails_to_process:     
            status = send_email(email)
            
        return len(self.emails_to_process)
    