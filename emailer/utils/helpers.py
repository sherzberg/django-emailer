from django.contrib.auth.models import User
from emailer.models import EmailBlast, EmailList
import datetime

def send_raw_email(email_obj, from_address, subject, content_html, send_after = None, just_prepare=False):
    '''
    Method to generically send a raw email with merge data. Use this method in your own apps to
    be able to track single emails. Could be for notifications or acknowledgements of events.
    This is a one off type email.
    '''

    email_list = EmailList()
    email_list.name = '%s - %s' %(str(datetime.datetime.now()),str(email_obj.email))
    email_list.data_raw_emails = email_obj.email
    email_list.is_oneoff = True
    email_list.type = EmailList.LISTTYPE_RAW_EMAILS
    email_list.save()

    email_blast = EmailBlast()
    email_blast.name = subject+ ' '+str(datetime.datetime.today().strftime("%Y-%b-%d-%m"))
    email_blast.send_after = send_after if send_after else datetime.datetime.now()
    email_blast.from_address = from_address
    email_blast.subject = subject
    email_blast.html = content_html
    email_blast.save()
    email_blast.lists.add(email_list)
    email_blast.save()

    email_blast.send(just_prepare)

def send_siteusers_email(user_objs, from_address, subject, content_html, send_after=None, just_prepare=False):
    '''
    Method to send email to a list of django.contrib.auth.models.Users. This should be
    used for one off type emails such as alerts or notifications.
    '''

    if not user_objs:
        raise Exception('There are no users to send to!')
    if not isinstance(user_objs[0], User):
        raise Exception('The users you provided are not django.contrib.auth.models.User objects')

    email_list = EmailList()
    email_list.name = '%s - %s' %(str(datetime.datetime.now()),str(subject))
    email_list.save()
    email_list.data_site_users = user_objs
    email_list.is_oneoff = True
    email_list.type = EmailList.LISTTYPE_SITEUSERS_USERDEFINED
    email_list.save()

    email_blast = EmailBlast()
    email_blast.name = subject+ ' '+str(datetime.datetime.today().strftime("%Y-%b-%d-%m"))
    email_blast.save()
    email_blast.lists = [email_list]
    email_blast.send_after = send_after if send_after else datetime.datetime.now()
    email_blast.from_address = from_address
    email_blast.subject = subject
    email_blast.html = content_html
    email_blast.save()

    email_blast.send(just_prepare)
