
from django.template import Context, Template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

import datetime
from html2text import html2text
from emailer.models import Email, EmailBlast
from urlparse import urljoin


def _append_tracking_image(html,tracking_url):
    html = html + '<img src="%s" alt="tracking url" />' %str(urljoin(settings.SITE_URL,tracking_url))
    return html

def _add_tracking_info(html, tracking_id, tracking_png_url):
    tracking_html = _append_tracking_image(html, tracking_png_url)
    
    return tracking_html

def _apply_merge_data(html, merge_data):
    t = Template(html)
    c = Context(merge_data)
    return t.render(c)
   
def _build_message(email):
    subject = email.subject
    from_email = email.from_address
    to = email.to_address
    
    merged_html = _apply_merge_data(email.html,{})
    
    text_content = html2text(merged_html)
    html_content = _add_tracking_info(merged_html, email.id, email.get_tracking_png_url())

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")

    return msg
    
def send_email(email):
    message = _build_message(email)
    
    try:
        message.send()
        email.status = Email.STATUS_SENT
    except Exception, e:
        email.status = Email.STATUS_ERRORED
        email.status_message = str(e)
        
    email.save()
    
    return email.status
    
def send_raw_email(to_address, from_address, subject, content_html, merge_data={}, just_prepare=False):
    '''
    Method to generically send a raw email with merge data. Use this method in your own apps to
    be able to track emails. Could be for notifications or acknowledgements of events.
    '''
    email_blast = EmailBlast()
    email_blast.name = subject+ ' '+str(datetime.datetime.today().strftime("%Y-%b-%d-%m"))
    email_blast.type = EmailBlast.BLASTTYPE_ONEOFF
    email_blast.send_after = datetime.datetime.now()
    email_blast.from_address = from_address
    email_blast.subject = subject
    email_blast.html = content_html
    email_blast.save()
    
    email = Email()
    email.email_blast = email_blast
    email.to_address = to_address
    email.merge_data = merge_data
    email.save()
    
    if not just_prepare:
        send_email(email)
        
    return email.status
