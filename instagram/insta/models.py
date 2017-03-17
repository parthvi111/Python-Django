from __future__ import unicode_literals
from choices import *
from django.db import models

# Create your models here.
class registermodl(models.Model):

	Name 	= models.CharField(max_length = 100)
	UserName 	= models.CharField(max_length = 100)    
	Password 	= models.CharField(max_length = 100)
	Email 		= models.CharField(max_length = 100)	
	Website 	= models.CharField(max_length =100)
	Bio 		= models.CharField(max_length =300)
	Phone_number = models.CharField(max_length =100)
	Gender 		=  models.IntegerField(choices=Gender_CHOICES, default=1)   
	Suggestions = models.BooleanField(False)
	Profile_pic = models.FileField(null = True , blank =True )
	account_type = models.CharField(max_length = 100)

	def __str__(self):
          return self.Password

class timelinemodl(models.Model):

	PostNo    = models.ForeignKey(registermodl, on_delete=models.CASCADE)
	Post      = models.CharField(max_length = 100)
	Post_time = models.DateTimeField(auto_now_add=True)
	Post_pic  = models.FileField(null = True , blank =True )

class friendmodl(models.Model):

	User_No = models.IntegerField()
	Friend_No = models.IntegerField()
	Request_status = models.BooleanField(default = False)
	Friend_status = models.BooleanField(default = False)

