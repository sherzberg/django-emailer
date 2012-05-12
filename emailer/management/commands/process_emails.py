
from django.core.management.base import BaseCommand, CommandError
from emailer.utils.processors import SimpleProcessor
import datetime

class Command(BaseCommand):
    args = "None"
    help = 'Process emails with SimpleProcessor'

    def handle(self, *args, **options):
        print datetime.datetime.now(), 'Starting SimpleProcessor'

        processor = SimpleProcessor()
                
        processor.prepare_emails()
        num_processed = processor.process_emails()
        
        print datetime.datetime.now(), 'SimpleProcessor Done: processed %d email(s)' %num_processed
        
