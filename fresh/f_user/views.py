from django.shortcuts import render
from models import *
from django.http import JsonResponse
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

	return render(request, 'f_user/login.html')

def register_ajax(request):
	list = UserInfo.objects.all()
	list2 = []
	for i in list:
		list2.append(i.uname)
	return JsonResponse({'data':list2})