from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
import os
import django

admin.autodiscover()

urlpatterns = patterns('',
    
    #emailer
    url(r'^emailer/', include('emailer.urls')),
    
    #tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    
    #admin
    #url(r'^admin/(.*)', admin.site.root),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
        'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)


if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$'%settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        (r'^(?P<path>.*xml)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT	+	'xml', 'show_indexes': True}),
        (r'^(?P<path>.*swf)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT	+	'flash', 'show_indexes': True}),
        (r'^(?P<path>.*jpg)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT	+	'images', 'show_indexes': True}),
	)


    admin_media_url = settings.STATIC_URL.lstrip('/') + '(?P<path>.*)$'
    admin_media_path = os.path.join(django.__path__[0], 'contrib', 'admin', 'media')
    print admin_media_path
    urlpatterns += patterns('',
        url(r'^' + admin_media_url , 'django.views.static.serve', {
            'document_root': admin_media_path,
        }, name='admin-media'),
    )
