from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.login),
	url(r'^register_ajax/$', views.register_ajax),
	url(r'^login_handle/$', views.login_handle),
	url(r'^$', views.index),
]