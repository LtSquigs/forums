from django.conf.urls.defaults import patterns, url

from forums import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)