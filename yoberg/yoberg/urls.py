from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yoberg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'yoscribe.views.home', name='home'),
<<<<<<< HEAD
    url(r'^twilio/', include('yosms.urls'))
=======
    url(r'^yo/', 'yoscribe.views.yo', name='yo'),
    url(r'^sms/', 'yoscribe.views.receiveSMS', name='sms'),
>>>>>>> ca88ababcda44d0c4dbfcdb6bf26fe80d59f2141
    url(r'^admin/', include(admin.site.urls)),
)
