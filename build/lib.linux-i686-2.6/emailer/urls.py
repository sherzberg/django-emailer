from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('emailer.views',
    
    url(r'^tracking/(?P<tracking_id>.+).png$', 'tracking', name='emailer-tracking_png'),
    url(r'^templates/$', 'templates', name='emailertemplate_list'),
    url(r'^template/(?P<template_id>.+)/$', 'template', name='emailer-template'),
    
)