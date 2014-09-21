from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^view/(?P<post_id>\d+)', views.view, name='view'),
	url(r'^.*', views.index, name='index'),)