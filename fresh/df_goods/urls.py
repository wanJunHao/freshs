from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^detail/$', views.detail),
	url(r'^list/$', views.list),
]