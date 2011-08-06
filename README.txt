django-emailer

v.1 - 2011-08-06

This django app is used to manage bulk (and one off) emails. You can create email templates,
and email lists. Emails can be created and bulk sent in a future date.

Required packages:
    - Python Image Library (PIL)
    
Optional Packages:
    - django-tinymce
    
Features (that currently work):
    - (manually) Create and edit model/objects in models.py
    - (manually) Send queue emails
    - (manually) Send one off emails. Used in generic forms or for event notifications on your site
    - Integrates with tinymce, just install django-tinymce and configure it appropriately
    - HTML and text content in emails
    - Tracking for opened emails (uses image requests for tracking so only possible for HTML clients)
    - South migrations
    
Future Features:
    - Create email lists
        - Query
        - User defined
        - Email signup, like newsletters and such
    - Email merge fields based on the email lists or any supplied merge data
    - Celery async email jobs
    - Notification signals (register signals for custom events and get emails)
    - Admin actions to process emails
    - Newsletter signups
    - Doctor direct links to the site to include tracking information which will
      provide tracking for people who paste links from text versions of the email
    
 Setup:
    - include in INSTALLED_APPS (settings.py)
        ...
        'emailer',
        ...
        
    - include in urls (urls.py)
        url(r'^emailer/', include('emailer.urls')),
        
    - if using django-tinymce, put this in the tinymce.init config (enables tiny-mce templates to use emailer templates):
        'template_external_list_url' : "emailer/templates/",
        
    - sync up your models, see django-south for more information
        $ python manage.py syncdb
        $ python manage.py migrate emailer
    
    
    
    
    
    