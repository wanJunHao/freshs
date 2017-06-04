from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^detail/$', views.detail),
	url(r'^list(\d+)_(\d*)_(\d*)/$', views.list),
	url(r'^detail(\d+)/$', views.detail),
	url(r'^place_order/$', views.place_order),
	url(r'^cart/$', views.cart),
]