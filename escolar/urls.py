from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
    #url(r'^$', 'core.views.home', name='home'),
    url(r'', include('accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
