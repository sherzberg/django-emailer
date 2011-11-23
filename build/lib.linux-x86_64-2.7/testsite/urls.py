from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    
    #emailer
    url(r'^emailer/', include('emailer.urls')),
    
    #tinymce
    url(r'^tinymce/', include('tinymce.urls')),
    
    #admin
    #url(r'^admin/(.*)', admin.site.root),
    url(r'^admin/', admin.site.urls),
    
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 
        'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
)
