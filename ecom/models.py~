# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import RegexValidator
# Create your models here.
class Category(models.Model):
	Name=models.CharField(max_length=30)
	Description=models.TextField(max_length=50)

	def __str__(self):
		return self.Name

class Product(models.Model):
	Categories=models.ForeignKey(Category,on_delete=models.CASCADE)
	Name=models.CharField(max_length=20,blank=True )
	Image=models.FileField(upload_to='media/',null=True,blank=True)
	IDorSNO=models.IntegerField(default=0,null=True,blank=True)
	Description=models.TextField(max_length=50,null=True,blank=True)
	Price=models.IntegerField(default=0,null=True,blank=True)
	NumbersAvailable=models.IntegerField(default=0,null=True,blank=True)

	def __str__(self):
		return self.Name

class CustomerDetail(models.Model):
	user = user=models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True)
        phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Phone number in the format: '+999999999'. Up to 11 digits allowed.")
	phonenumber=models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
	Email=models.CharField(max_length=30, blank=True)
	ShippingAddress=models.TextField(max_length=50, blank=True, null=True)
	City=models.CharField(max_length=20,blank=True)
	State=models.CharField(max_length=20,blank=True)
	Landmark=models.CharField(max_length=30,blank=True)
	Pincode=models.IntegerField(default=0, blank=True, null=True)

	def __str__(self):
			return self.user.username

class Order(models.Model):
	user = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE, blank=True, null=True)
	totalamount = models.IntegerField(blank=True, null=True, default=0)
	checkout_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
			return self.user.user.username


class Cartm(models.Model):
	order = models.ForeignKey(Order, related_name="cartorder", on_delete=models.CASCADE, blank=True, null=True)
	product =models.ForeignKey(Product, blank=True, null=True)
	quantity = models.IntegerField(null=True, blank=True)
	amount =models.IntegerField(default=0,null=True,blank=True)

	def __str__(self):
			return self.product.Name

class Cartmodel(models.Model):
	cart=models.OneToOneField(Product, on_delete=models.CASCADE)
	quantity=models.IntegerField()


class Cartprto(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)


	def __str__(self):
		return self.User.username


class Cartitem(models.Model):
	cart=models.ForeignKey(Cartm, on_delete=models.CASCADE)
	product=models.ManyToManyField(Cartmodel)
