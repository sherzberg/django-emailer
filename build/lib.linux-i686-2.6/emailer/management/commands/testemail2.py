
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from emailer.utils import send_raw_email 
        
class Command(BaseCommand):
    args = "None"
    help = 'Process emails with SimpleProcessor'

    def handle(self, *args, **options):
        from_address = 'test@gmail.com'
        subject = 'one off test'
        
        html = '<p>Hello</p>lksjdlfkdj'
        
#        u = User.objects.all()[0]:
#            if u.email != '':
#                send_raw_email(u, from_address, subject, html)
#        
        print 'test sent'
        