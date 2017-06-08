from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
	ttitle = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	def __str__(self):
		return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
	gtitle = models.CharField(max_length=20)
	gpic = models.ImageField(upload_to='goods')
	gprice = models.DecimalField(max_digits=5,decimal_places=2)
	isDelete = models.BooleanField(default=False)
	gunit = models.CharField(max_length=20,default='500g')
	gclick = models.IntegerField()
	gjianjie = models.CharField(max_length=200)
	gkucun = models.IntegerField()
	gcontent = HTMLField()
	gtype = models.ForeignKey('TypeInfo')
	def __str__(self):
		return self.gtitle.encode('utf-8')

class CartInfo(models.Model):
	uid = models.IntegerField()
	gid = models.IntegerField()
	gs = models.IntegerField()
	class Meta:
		db_table = 'cartinfo'

class OrderInfo(models.Model):
	uid = models.IntegerField()
	gid = models.IntegerField()
	gs = models.IntegerField()
	ispay = models.BooleanField(default=False)
	class Meta:
		db_table = 'orderinfo'