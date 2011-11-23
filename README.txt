django-emailer

v.1 - 2011-08-13

This django app is used to manage bulk (and one off) emails. You can create email templates,
and email lists. Emails can be created and bulk sent in a future date.

Required packages:
    - Python Image Library (PIL)
    - South
    
Optional Packages:
    - django-tinymce
    
Features (that currently work):
    - Create EmailLists:
        - Site users (list of auth.models.user objects)
        - Raw email addresses (list of comma separated emails)
    - Create EmailBlasts. Allows you to send email to EmailLists.
    - Merge fields. Uses standard djangos template processor to fill in merge fields.
    - Integrates with tinymce, just install django-tinymce and configure it appropriately
    - HTML and text content in emails (uses html2text to generate the text content)
    - Tracking for opened emails (currently uses html image requests for tracking so only possible for HTML clients)
    
Future Features:
    - EmailLists
        - Custom sql query (query for email address and merge data)
    - Celery async email jobs
    - Admin actions to process emails
    - Doctor direct links to the site to include tracking information which will
      provide tracking for people who paste links from text versions of the email
    
 Setup:
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
    
    
    
    
    
    
