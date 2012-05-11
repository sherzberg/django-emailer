================
django-emailer
================
v.2 - 2012-05-10
----------------

**This software should be considered beta. However, I do use the email templates, lists, and bulk emails on a daily production site for a limited amount of emails per week.**

This django app is used to manage bulk (and one off) emails. You can create email templates,
and email lists. Emails can be created and bulk sent in a future date.

*Required packages:*
 - Django (1.4)
 - Python Image Library (PIL) (1.1.7)
 - South (0.7.5)
    
*Optional Packages:*
- django-tinymce
    
**Features (that currently work):**
 - EmailLists:
    - Site users (list of auth.models.user objects)
    - Raw email addresses (list of comma separated emails)
 - EmailBlasts:
    - Allows you to send email to EmailLists.
 - Merge fields
    - Uses standard djangos template processor to fill in merge fields.
 - Integrates with tinymce, just install django-tinymce and configure it appropriately
 - HTML and text content in emails (uses html2text to generate the text content)
 - Tracking for opened emails (currently uses html image requests for tracking so only possible for HTML clients)
    
**Future Features:**
 - EmailLists
    - Custom sql query (query for email address and merge data)
 - Celery async email jobs
 - Admin actions to process emails
 - Doctor direct links to the site to include tracking information which will provide tracking for people who paste links from text versions of the email
  

**Setup:**
 - include in INSTALLED_APPS (settings.py)
    ...
    'django.contrib.sites',
    'south',
    ...
    'emailer',
    ...
        
 - include in urls (urls.py)
    url(r'^emailer/', include('emailer.urls')),
        
 - if using django-tinymce, put this in the tinymce.init config (enables tiny-mce templates to use emailer templates):
    'template_external_list_url' : "emailer/templates/",
    
 - update site instance in the admin to reflect your site, see the django docs for this
    
 - sync up your models, see django-south for more information
    $ python manage.py syncdb
    $ python manage.py migrate emailer
    
    
    
    
    
    
