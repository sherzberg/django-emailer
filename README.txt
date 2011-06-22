django-emailer

v.1 - 2011-06-21

This django app is used to manage bulk (and one off) emails. You can create email templates,
and email lists. Emails can be created and bulk sent in a future date.

Features (that currently work):
    - (manually) Create and edit model/objects in models.py
    - (manually) Send queue emails
    - (manually) Send one off emails. Used in generic forms or for event notifications on your site
    - Integrates with tinymce, just install django-tinymce and configure it appropriately
    - HTML and text content in emails
    - Tracking for opened emails (uses image requests for tracking so only possible for HTML clients)
    
Future Features:
    - Create email lists
        - Query
        - User defined
        - Email signup, like newsletters and such
    - Celery async email jobs
    - Notification signals (register signals for custom events and get emails)
    - Admin actions to process emails
    - Newsletter signups
    