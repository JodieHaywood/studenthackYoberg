from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yoberg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'yoscribe.views.home', name='home'),
    url(r'^yo/$', 'yoscribe.views.yo', name='yo'),
    url(r'^sms/$', 'yoscribe.views.receiveSMS', name='sms'),
)
