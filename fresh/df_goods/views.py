from django.shortcuts import render
from models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):

	context = {}

	for i in range(1,7):
		context['a'+str(i)] = GoodsInfo.objects.filter(gtype_id=i).order_by('-gclick')[0:3]
		context['aa'+str(i)] = GoodsInfo.objects.filter(gtype_id=i).order_by('-id')[0:4]
	return render(request,'df_goods/index.html',context)

	

def list(request,pid,yid):
	glist = GoodsInfo.objects.filter(gtype_id=pid).order_by('-id')
	p = Paginator(glist,10)
	page = p.page(yid)
	context = {'page':page,'pid':pid}
	return render(request,'df_goods/list.html',context)

def detail(request):
	context = {}
	return render(request,'df_goods/detail.html',context)