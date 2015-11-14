from django.contrib import admin
from django.db import models


# Register your models here.

class SignUp(models.Model):
	first_name = models.CharField(max_length=120,null=True,blank=True)
	last_name = models.CharField(max_length=120,null=True,blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	update = models.DateTimeField(auto_now_add=False,auto_now=True)

	