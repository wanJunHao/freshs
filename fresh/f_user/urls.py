from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.login),
	url(r'^register_ajax/$', views.register_ajax)
]