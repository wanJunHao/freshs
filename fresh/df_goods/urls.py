from django.conf.urls import url 
import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^list(\d+)_(\d*)_(\d*)/$', views.list),
	url(r'^detail(\d+)/$', views.detail),
	url(r'^add(\d+)_(\d+)/$', views.add),
	url(r'^cart/$', views.cart),
	url(r'^jia/$', views.jia),
	url(r'^place_order/$', views.place_order),
	url(r'^place_order(\d+)/$', views.now_buy),
	# url(r'^goods/search/$', views.MySearchView),
]