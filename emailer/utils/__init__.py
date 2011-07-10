
from emailer.models import EmailBlast, EmailList

import datetime



def send_raw_email(email_obj, from_address, subject, content_html, just_prepare=False):
    '''
    Method to generically send a raw email with merge data. Use this method in your own apps to
    be able to track single emails. Could be for notifications or acknowledgements of events.
    '''

    email_list = EmailList()
    email_list.name = '%s - %s' %(str(datetime.datetime.now()),str(email_obj.email))
    email_list.data_raw_emails = email_obj.email
    email_list.is_oneoff = True
    email_list.type = EmailList.LISTTYPE_RAW_EMAILS
    email_list.save()
    
    email_blast = EmailBlast()
    email_blast.name = subject+ ' '+str(datetime.datetime.today().strftime("%Y-%b-%d-%m"))
    email_blast.lists = [email_list]
    email_blast.send_after = datetime.datetime.now()
    email_blast.from_address = from_address
    email_blast.subject = subject
    email_blast.html = content_html
    email_blast.save()
    
    if just_prepare:
        status = email_blast.prepare_for_send()
    else:
        status = email_blast.send_now()
        
    return status

def send_siteusers_email(user_objs, from_address, subject, content_html, just_prepare=False):
    '''
    Method to generically send a raw email with merge data. Use this method in your own apps to
    be able to track single emails. Could be for notifications or acknowledgements of events.
    '''

    email_list = EmailList()
    email_list.name = '%s - %s' %(str(datetime.datetime.now()),str(subject))
    email_list.data_site_users = user_objs
    email_list.is_oneoff = True
    email_list.type = EmailList.LISTTYPE_SITEUSERS_USERDEFINED
    email_list.save()
    
    email_blast = EmailBlast()
    email_blast.name = subject+ ' '+str(datetime.datetime.today().strftime("%Y-%b-%d-%m"))
    email_blast.lists = [email_list]
    email_blast.send_after = datetime.datetime.now()
    email_blast.from_address = from_address
    email_blast.subject = subject
    email_blast.html = content_html
    email_blast.save()
    
    if just_prepare:
        status = email_blast.prepare_for_send()
    else:
        status = email_blast.send_now()
        
    return status