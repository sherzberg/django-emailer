

from django.core.management.base import BaseCommand, CommandError

from emailer.utils.emailprocessors import SimpleProcessor      
        
class Command(BaseCommand):
    args = "None"
    help = 'Process emails with SimpleProcessor'

    def handle(self, *args, **options):
        
        processor = SimpleProcessor()
                
        processor.prepare_emails()
        num_processed = processor.process_emails()
        
        print 'Done: processed %d' %num_processed
        
        