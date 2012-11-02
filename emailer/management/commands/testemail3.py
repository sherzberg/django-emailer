
from django.conf import settings
from django.core.management.base import BaseCommand

from emailer.utils import send_siteusers_email
from django.contrib.auth.models import User

class Command(BaseCommand):
    args = "None"
    help = 'Process emails with SimpleProcessor'

    def handle(self, *args, **options):
        class RawEmail():
            def __init__(self, email):
                self.email = email
                
        to_address = settings.ADMINS[0][1]
        from_address = 'test@gmail.com'
        subject = 'one off test - just prepared'
        
        html = '''<p>This message was sent to: {{ email }}</p>'''
        
        user = User.objects.all()[0]

        send_siteusers_email(
                [user],
                from_address,
                subject,
                html,
                just_prepare=True
                )

        print 'test prepared'
