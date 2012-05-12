================
django-emailer
================
v.2 - 2012-05-10
----------------

**This software should be considered beta. However, I do use the email templates, lists, and bulk emails on a daily production site for a limited amount of emails per week.**

This django app is used to manage bulk (and one off) emails. You can create email templates,
and email lists. Emails can be created and bulk sent in a future date.

Requirements
============

django-emailer is tested with:

* Django (1.4)
* Python Image Library (PIL) (1.1.7)
* South (0.7.5)
* django-tinymce
    
Features (that currently work):
===============================
* EmailLists:
   * Site users (list of auth.models.user objects)
   * Raw email addresses (list of comma separated emails)
* EmailBlasts:
   * Allows you to send email to EmailLists.
* Merge fields
   * Uses standard django template processor to fill in merge fields.
* Integrates with tinymce, just install django-tinymce and configure it appropriately
* HTML and text content in emails (uses html2text to generate the text content)
* Tracking for opened emails (currently uses html image requests for tracking so only possible for HTML clients)
    
Future Features:
================
* EmailLists
    - Custom sql query (query for email address and merge data)
* Celery async email jobs
* Admin actions to process emails
* Doctor direct links to the site to include tracking information which will provide tracking for people who paste links from text versions of the email


Install:
========
You can use the setup.py file to install:

::
    python setup.py install

Or you can use pip and install from the github repository:

::
    pip install -e git+git://github.com/whelmingbytes/django-emailer.git#egg=django-emailer

Setup:
======
* include in INSTALLED_APPS (settings.py)

::

    ...
    'emailer',
    ...

* setup smtp settings (settings.py)

::

    ...
    EMAIL_HOST_USER = 'test@myshost.com'
    EMAIL_HOST = '127.0.0.1'
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
    ...

* include in urls (urls.py)

::

    url(r'^emailer/', include('emailer.urls')),
        
* if using django-tinymce, put this in the tinymce.init config (enables tiny-mce templates to use emailer templates):

::

    'template_external_list_url' : "emailer/templates/",
    
* update site instance in the admin to reflect your site, see the django docs for this
    
* sync up your models, see django-south for more information

::

    $ python manage.py syncdb
    $ python manage.py migrate emailer


Use it:
=======
Using the utility helper functions is the fastest way to send email:

::

    from emailer.utils import send_siteusers_email
    from django.contrib.auth.models import User

    users_to_send_to = User.objects.filter(email__contains='oo')

    subject = 'Simple Test Email'
    from = 'no-reply@myhost.com'
    content = '<h1>Hello!</h1> This is a test email.'

    #This will send an email to all users with 'oo' in their email address from
    #the users table. This will block until the email is sent.
    send_siteusers_email(users_to_send_to, subject, from, content)

