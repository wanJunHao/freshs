from django.db import models

# Create your models here.

class UserInfo(models.Model):
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=40)
	uemail = models.CharField(max_length=20)
	uaddr = models.CharField(max_length=100)
	utel = models.CharField(max_length=11)
	uzip_code = models.CharField(max_length=6)
