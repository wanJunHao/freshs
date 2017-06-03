from django.shortcuts import render
from models import *
# Create your views here.

def index(request):

	click_list1 = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
	new_list1 = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
	c1 = []
	n1 = []	
	for i in click_list1:
		c1.append({'id':i.id,'title':i.gtitle[0:8]+'...'})
	for j in new_list1:
		n1.append({'title':j.gtitle[0:8]+'...','img':j.gpic,'price':j.gprice})

	click_list2 = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[0:3]
	new_list2 = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[0:4]
	c2 = []
	n2 = []	
	for i in click_list2:
		c2.append({'id':i.id,'title':i.gtitle[0:8]+'...'})
	for j in new_list2:
		n2.append({'title':j.gtitle[0:8]+'...','img':j.gpic,'price':j.gprice})

	click_list3 = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:3]
	new_list3 = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
	c3 = []
	n3 = []	
	for i in click_list3:
		c3.append({'id':i.id,'title':i.gtitle[0:8]+'...'})
	for j in new_list3:
		n3.append({'title':j.gtitle[0:8]+'...','img':j.gpic,'price':j.gprice})

	click_list4 = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:3]
	new_list4 = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
	c4 = []
	n4 = []	
	for i in click_list4:
		c4.append({'id':i.id,'title':i.gtitle[0:8]+'...'})
	for j in new_list4:
		n4.append({'title':j.gtitle[0:8]+'...','img':j.gpic,'price':j.gprice})

	click_list5 = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:3]
	new_list5 = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
	c5 = []
	n5 = []	
	for i in click_list5:
		c5.append({'id':i.id,'title':i.gtitle[0:8]+'...'})
	for j in new_list5:
		n5.append({'title':j.gtitle[0:8]+'...','img':j.gpic,'price':j.gprice})

	click_list6 = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[0:3]
	new_list6 = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]
	c6 = []
	n6 = []	
	for i in click_list6:
		c6.append({'id':i.id,'title':i.gtitle[0:8]+'...'})
	for j in new_list6:
		n6.append({'title':j.gtitle[0:8]+'...','img':j.gpic,'price':j.gprice})
	
	context = {
			'c1':c1,'n1':n1,
			'c2':c2,'n2':n2,
			'c3':c3,'n3':n3,
			'c4':c4,'n4':n4,
			'c5':c5,'n5':n5,
			'c6':c6,'n6':n6
	}

	return render(request,'df_goods/index.html',context)

	

def list(request):
	context = {}
	return render(request,'df_goods/list.html',context)

def detail(request):
	pass