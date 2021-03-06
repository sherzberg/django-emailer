import logging
logger = logging.getLogger('emailer.utils.processors')

from emailer.models import Email
import datetime

class AbstractProcessor():

    def prepare_emails(self):
        '''
        Does any prep work on the emails.
        '''
        raise NotImplementedError()

    def process_emails(self):
        '''
        Needs to process and send the emails. Returns the number sent.
        '''
        raise NotImplementedError()

class SimpleProcessor(AbstractProcessor):
    '''
    A simple email processor that batch sends 50 unsent emails at once.
    This may block for a while and is meant to be run on a cron job.
    '''

    def prepare_emails(self):
        pass

    def process_emails(self):
        logger.debug('Starting to process email blasts')

        emails = Email.objects.filter(status=Email.STATUS_PREPARED)
        logger.debug("Emails: "+str(len(emails.all())))
        emails = emails.filter(email_blast__send_after__lte=datetime.datetime.now())[:50]
        
        logger.debug('Attempting to process %d emails', len(emails))
        for email in emails:
            email.send()
        
        return len(emails)
