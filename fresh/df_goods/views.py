#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
	types = TypeInfo.objects.all()
	list1 = []
	for i in types:
		list1.append({
		          'type':i,
		          'click_list':i.goodsinfo_set.order_by('-gclick')[0:3],
		          'new_list':i.goodsinfo_set.order_by('-id')[0:4],
		})

	context = {'list':list1}
	return render(request,'df_goods/index.html',context)

	

def list(request,pid,yid,orderby):
	types = TypeInfo.objects.all()
	ltitle = TypeInfo.objects.filter(id=pid)[0].ttitle
	
	# 通过get传值设置session来判断需要哪儿种排序
	
	
	glist = GoodsInfo.objects.filter(gtype_id=pid)
	if orderby == '1':
		glist = glist.order_by('-id')
	elif orderby == '2':
		glist = glist.order_by('-gprice')
	else:
		glist = glist.order_by('-gclick')
	# if a=='price':
	# 	request.session['aa']='price'
	# elif a=='people':
	# 	request.session['aa']='people'
	# elif a=='default':
	# 	request.session['aa']='default'

	# if 'aa' in request.session:
	# 	if request.session['aa']=='price':
	# 		glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-gprice')
	# 	elif request.session['aa']=='people':
	# 		glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-gclick')
	# 	else:
	# 		glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')

	# else:
	# 	glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')
	new_list = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')[0:2]
	p = Paginator(glist,10)
	page = p.page(yid)
	context = {'page':page,'pid':pid,'types':types,'title':ltitle,'new_list':new_list,'orderby':orderby}
	return render(request,'df_goods/list.html',context)

def detail(request,pid):
	
	good = GoodsInfo.objects.get(id=pid)
	new_list = GoodsInfo.objects.filter(gtype_id=good.gtype.id).order_by('-id')[0:2]

	context = {'good':good,'list':new_list}
	return render(request,'df_goods/detail.html',context)

def place_order(request):
	
	name = request.session['uname']
	context = {'name':name}

	return render(request, 'df_goods/place_order.html', context)

def cart(request):
	uid = request.session.get('uid','hi')
	
	if uid == 'hi':
		return redirect('/user/login/')

	else:
		name = request.session['uname']
		context = {'name':name}
	
	return render(request, 'df_goods/cart.html', context)