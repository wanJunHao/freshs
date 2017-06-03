from django.shortcuts import render
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

	

def list(request,pid,yid):
	types = TypeInfo.objects.all()
	ltitle = TypeInfo.objects.filter(id=pid)[0].ttitle
	

	dict = request.GET
	a = dict.get('a','')	
	if a=='price':
		request.session['aa']='price'
	elif a=='people':
		request.session['aa']='people'
	elif a=='':
		request.session['aa']=''

	if request.session['aa']=='price':
		glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-gprice')
	elif request.session['aa']=='people':
		glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-gclick')
		
	else:
		glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')
	new_list = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')[0:2]
	p = Paginator(glist,10)
	page = p.page(yid)
	context = {'page':page,'pid':pid,'types':types,'title':ltitle,'new_list':new_list}
	return render(request,'df_goods/list.html',context)

def detail(request,pid):
	good = GoodsInfo.objects.get(id=pid)
	new_list = GoodsInfo.objects.filter(gtype_id=good.gtype.id).order_by('-id')[0:2]
	context = {'good':good,'list':new_list}
	return render(request,'df_goods/detail.html',context)
