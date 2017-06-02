from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.login),
	url(r'^register_ajax/$', views.register_ajax),
	url(r'^login_handle/$', views.login_handle),
	url(r'^$', views.index),
	url(r'^user_info/$', views.user_info),
	url(r'^name/$', views.name),
	url(r'^logout/$', views.logout),
	url(r'^user_order/$', views.user_order),
	url(r'^user_site/$', views.user_site),
	url(r'^user_set/$', views.user_set),
]