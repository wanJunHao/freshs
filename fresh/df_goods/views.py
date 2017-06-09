#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from f_user.models import *
# Create your views here.

def index(request):
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		count = '哼'
	else:
		count = len(CartInfo.objects.filter(uid=uid))

	types = TypeInfo.objects.all()
	list1 = []
	for i in types:
		list1.append({
		          'type':i,
		          'click_list':i.goodsinfo_set.order_by('-gclick')[0:3],
		          'new_list':i.goodsinfo_set.order_by('-id')[0:4]
		})

	context = {'list':list1,'count':count}
	return render(request,'df_goods/index.html',context)

	

def list(request,pid,yid,orderby):
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		count = '哼'
	else:
		count = len(CartInfo.objects.filter(uid=uid))

	types = TypeInfo.objects.all()
	ltitle = TypeInfo.objects.filter(id=pid)[0].ttitle
	
	glist = GoodsInfo.objects.filter(gtype_id=pid)
	if orderby == '1':
		glist = glist.order_by('-id')
	elif orderby == '2':
		glist = glist.order_by('-gprice')
	else:
		glist = glist.order_by('-gclick')
	
	new_list = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')[0:2]
	p = Paginator(glist,10)
	page = p.page(yid)
	context = {'page':page,'pid':pid,'types':types,'title':ltitle,'new_list':new_list,'orderby':orderby,'count':count}
	return render(request,'df_goods/list.html',context)

def detail(request,pid):
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		count = '哼'
	else:
		count = len(CartInfo.objects.filter(uid=uid))
	types = TypeInfo.objects.all()
	good = GoodsInfo.objects.get(id=pid)
	new_list = GoodsInfo.objects.filter(gtype_id=good.gtype.id).order_by('-id')[0:2]

	context = {'good':good,'list':new_list,'count':count}
	return render(request,'df_goods/detail.html',context)

def cart(request):
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		return redirect('/user/login/')
	else:
		name = request.session['uname']
	
	ggg = []
	list1 = CartInfo.objects.filter(uid=uid)
	for i in list1:
		ggg.append({
				'good':GoodsInfo.objects.get(id=i.gid),
				'num':i.gs,
				'id':i.id
		})
	
	context = {'ggg':ggg,'name':name,'page_num':2}		
	return render(request, 'df_goods/cart.html', context)

def add(request,gid,count):
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		return redirect('/user/login/')
	else:
		list1 = CartInfo.objects.filter(uid=uid).filter(gid=gid)
		if len(list1) == 0:
			a = CartInfo()
			a.gid = gid
			a.uid = uid
			a.gs = int(count)
			a.save()
		else:
			list1[0].gs += int(count)
			list1[0].save()
		if request.is_ajax():
			list2 = CartInfo.objects.filter(uid=uid)
			return JsonResponse({'num':len(list2)})
		else:
			return redirect('/goods/cart/')

def place_order(request):

	name = request.session['uname']
	cids = request.GET.getlist('cid')
	uid = request.session.get('uid')
	user = UserInfo.objects.get(id=uid)
	list1 = []
	for i in cids:
		list2 = CartInfo.objects.all()
		for j in list2:
			if j.id == int(i):
				list1.append({
				'good':GoodsInfo.objects.get(id=CartInfo.objects.get(id=i).gid),
				'gs':CartInfo.objects.get(id=i).gs,
				'id':i
			})
	context = {'name':name,'user':user,'list':list1,'page_num':2}
	return render(request,'df_goods/place_order.html',context)

from haystack.views import SearchView
# class MySearchView(SearchView):
#     def extra_context(self):
#         extra = super(FacetedSearchView, self).extra_context()
#         extra['title'] = self.request.GET.get('q')
#         return extra

def plus(request):
	
	gid = request.GET.get('gid')
	uid = request.session.get('uid')
	list1 = CartInfo.objects.filter(uid=uid).filter(gid=gid)
	a = list1[0]
	if a.gs < 100:
		a.gs += 1
		a.save()

def reduce(request):
	
	gid = request.GET.get('gid')
	uid = request.session.get('uid')
	list1 = CartInfo.objects.filter(uid=uid).filter(gid=gid)
	a = list1[0]
	if a.gs > 1:
		a.gs -= 1
		a.save()

def delete(request):

	cid = request.GET.get('cid')
	cartinfo = CartInfo.objects.get(id=cid)
	cartinfo.delete()

	return JsonResponse({'areuok':'ok'})

# def pay_now(request,gid,gs):
# 	uid = request.session.get('uid','hi')
# 	if uid == 'hi':
# 		return redirect('/user/login/')
# 	else:
# 		name = request.session['uname']
# 		user = UserInfo.objects.get(id=uid)
		
# 		list1 = [{
# 			'good':GoodsInfo.objects.get(id=gid),
# 			'gs':gs
# 				}]
# 		context = {'name':name,'user':user,'list':list1,'page_num':2}
# 		return render(request, 'df_goods/place_order.html', context)