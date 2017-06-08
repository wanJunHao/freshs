from django.shortcuts import render,redirect
from django.db import transaction
from django.http import HttpResponse
from models import OrderInfo,OrderDetailInfo
from df_goods.models import GoodsInfo,CartInfo
from datetime import datetime

# Create your views here.

@transaction.atomic
def order(request):
	name = request.session['uname']
	post = request.POST
	addr = post.get('address')
	cids = post.getlist('cid')

	sid = transaction.savepoint()
	try:
		order = OrderInfo()
		now = datetime.now()
		uid = request.session['uid']
		order.oid = '%s%d' % (now.strftime('%Y%m%d%H%M%S'), uid)
		order.user_id = uid
		order.odate = now
		order.oaddress = addr 
		order.ototal = 0
		order.save()

		ototal = 0
		for i in cids:
			cart = CartInfo.objects.get(id=i)
			if cart.gs > GoodsInfo.objects.get(id=cart.gid).gkucun:
				transaction.savepoint_rollback(sid)
				return redirect('/goods/cart/')
			else:
				a = GoodsInfo.objects.get(id=cart.gid)
				a.gkucun -= cart.gs
				a.save()
				order_detail = OrderDetailInfo()
				order_detail.order = order
				order_detail.goods = GoodsInfo.objects.get(id=cart.gid)
				order_detail.price = GoodsInfo.objects.get(id=cart.gid).gprice
				order_detail.count = cart.gs				
					
				order_detail.save()				
				ototal += order_detail.price*order_detail.count
				cart.delete()
		order.ototal = ototal
		order.save()

		transaction.savepoint_commit(sid)
		return redirect('/user/user_order1/')

	except:
	
		transaction.savepoint_rollback(sid)
		return redirect('/goods/cart/')

def pay(request,oid):
	a = OrderInfo.objects.get(oid=oid)
	a.oIsPay = True
	a.save()
	return redirect('/user/user_order1/')