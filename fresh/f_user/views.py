#coding=utf-8
from django.shortcuts import render,redirect
from models import *
from df_goods.models import GoodsInfo,CartInfo
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.core.paginator import Paginator
from df_order.models import OrderInfo,OrderDetailInfo
# Create your views here.

def register(request):
	return render(request, 'f_user/register.html')

def login(request):
	user = request.POST
	if user.get('pwd') != None:
		
		tom = UserInfo()
		tom.uname = user.get('user_name')
		tom.upwd = user.get('pwd')
		tom.uemail = user.get('email')
		tom.save()
	name = request.COOKIES.get('name','')
	a = 0
	if name == '':
		a = 1

	return render(request, 'f_user/login.html',{'name':name,'dat':0,'a':a})

def register_ajax(request):

	list = UserInfo.objects.all()
	list2 = []
	for i in list:
		list2.append(i.uname)
	return JsonResponse({'data':list2})

def login_handle(request):
	dict = request.POST
	name = dict.get('username')
	pwd = dict.get('pwd')
	rem = dict.get('remember')
	users = UserInfo.objects.filter(uname=name)
	
	if len(users) == 1:
		if users[0].upwd == pwd:

			url = request.COOKIES.get('url','/')
			red = HttpResponseRedirect(url)
			red.set_cookie('url','',max_age=-1)

			if rem=='1':				
				red.set_cookie('name',name)
			else:
				red.set_cookie('name','',max_age=-1)

			request.session['uid'] = users[0].id
			request.session['uname'] = name
			# request.session.set_expiry(0)
			return red

		else:
			return render(request,'f_user/login.html',{'dat':1})
	
	return render(request,'f_user/login.html',{'dat':2})

def user_info(request):
	
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		return redirect('/user/login/')
	else:
		users = UserInfo.objects.filter(id=uid)
		name = users[0].uname
		tel = users[0].utel
		addr = users[0].uaddr

		if request.COOKIES.has_key(name):
			a = request.COOKIES[name].split('%2C')
			see_list = []
			for i in a:
				see_list.append({ 
				    'see' : GoodsInfo.objects.get(id=int(i))
				})

			context = {'name':name,'tel':tel,'addr':addr,'see_list':see_list,'page_num':2}
		else:
			context = {'name':name,'tel':tel,'addr':addr,'page_num':2}
		
		return render(request,'f_user/user_info.html',context)


def name(request):
	name = request.session['uname']
	return JsonResponse({'name':name})

def logout(request):
	request.session.flush()
	return redirect('/')

def user_order(request,index):

	uid = request.session.get('uid','hi')
	if uid == 'hi':
		return redirect('/user/login/')
	else:
		name = request.session.get('uname')
		list1 = OrderInfo.objects.filter(user_id=uid)[::-1]

		p = Paginator(list1,2)
		page = p.page(index)
		

	context = {'name':name,'page':page,'page_num':2}

	return render(request, 'f_user/user_order.html',context)

def user_site(request):
	name = request.session['uname']

	uid = request.session['uid']
	a = UserInfo.objects.get(id=uid)
	tel = a.utel
	get_name = a.get_name
	zip_code = a.uzip_code
	addr = a.uaddr
	if tel !='':
		return render(request, 'f_user/user_site.html',{'num':1,'a':a,'page_num':2,'name':name})
	
	return render(request, 'f_user/user_site.html',{'name':name,'num':0,'page_num':2})

def user_set(request):
	name = request.session['uname']
	uid = request.session['uid']
	a = UserInfo.objects.get(id=uid)

	dict = request.POST
	get_name = dict.get('get_name')
	tel = dict.get('tel')
	zip_code = dict.get('zip_code')
	addr = dict.get('site_area')


	a.utel = tel
	a.get_name = get_name
	a.uzip_code = zip_code
	a.uaddr = addr
	a.save()


	
	return render(request, 'f_user/user_site.html',{'num':1,'a':a,'page_num':2,'name':name})

def car_data(request):
	uid = request.session.get('uid','hi')
	if uid == 'hi':
		return JsonResponse({'count':'哼'})
	else:
		list1 = CartInfo.objects.filter(uid=uid)
		return JsonResponse({'count':len(list1)})