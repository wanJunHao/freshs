from django.shortcuts import render,redirect
from models import *
from django.http import JsonResponse,HttpResponseRedirect
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
	print rem 
	
	if len(users) == 1:
		if users[0].upwd == pwd:

			url = request.COOKIES.get('url','/user/')
			red = HttpResponseRedirect(url)
			red.set_cookie('url','',max_age=-1)

			if rem=='1':				
				red.set_cookie('name',name)
			else:
				red.set_cookie('name','',max_age=-1)
			return red

		else:
			return render(request,'f_user/login.html',{'dat':1})
	
	return render(request,'f_user/login.html',{'dat':2})

def index(request):
	return render(request,'f_user/index.html')

