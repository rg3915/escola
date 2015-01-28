from django.conf.urls import url
from django.conf.urls import patterns
from django.contrib.flatpages import views
from accounts import views


urlpatterns = patterns('accounts.views',
	url(r'^$', 'home'),
    url(r'^professores/$', 'p_login'),
    url(r'^validar/$', 'validar'),
    url(r'^logoff/$', 'logoff'),
    url(r'^professor/$', 'professor'),

)