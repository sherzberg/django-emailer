

from django.core.management.base import BaseCommand

from emailer.utils import send_raw_email 
        
class Command(BaseCommand):
    args = "None"
    help = 'Process emails with SimpleProcessor'

    def handle(self, *args, **options):
        
        to_address = 'spencer.herzberg@gmail.com'
        from_address = 'test@gmail.com'
        subject = 'one off test'
        
        html = '<p>Hello</p>lksjdlfkdj'
        
        send_raw_email(to_address, from_address, subject, html)
        print 'test sent'