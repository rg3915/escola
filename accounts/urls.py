from django.conf.urls import patterns, include, url
from django.contrib.flatpages import views
# from accounts.views import *


urlpatterns = patterns('accounts.views',
                       url(r'^$', 'home'),
                       url(r'^professores/$', 'p_login'),
                       url(r'^validar/$', 'validar'),
                       url(r'^logoff/$', 'logoff'),
                       url(r'^professor/$', 'professor'),

                       )
