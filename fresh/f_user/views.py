from django.shortcuts import render

# Create your views here.

def register(request):
	return render(request, 'f_user/register.html')