from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^list(\d+)_(\d*)_(\d*)/$', views.list),
	url(r'^detail(\d+)/$', views.detail),
	url(r'^add(\d+)_(\d+)/$', views.add),
	url(r'^cart/$', views.cart),
	url(r'^place_order/$', views.place_order),
	# url(r'^goods/search/$', views.MySearchView),
	url(r'^plus/$', views.plus),
	url(r'^reduce/$', views.reduce),
	url(r'^delete/$', views.delete),
	# url(r'^pay_now(\d+)_(\d+)/$', views.pay_now),

]