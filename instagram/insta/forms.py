from django import forms
from .models import registermodl
from .choices import *


class ImageUploadForm(forms.Form):
    	image = forms.FileField()


class Edit_form(forms.Form):
		  
		Name = forms.CharField(max_length =100)
		UserName = forms.CharField(max_length =100)
		Website = forms.CharField(max_length =100)
		Bio = forms.CharField(widget=forms.Textarea)
		Email = forms.CharField(max_length =100)
		Phone_number = forms.CharField(max_length =100)
		Gender = forms.ChoiceField(choices = Gender_CHOICES , label="", initial ="" ,widget=forms.Select() ,required =True)
		Suggestions = forms.BooleanField(False)

class TimeLinePostForm(forms.Form):
		Name = forms.CharField(max_length =100)
		post_image = forms.ImageField()

class RegistrationForm(forms.Form):
		Name 	= forms.CharField(max_length = 100,required =True)
		UserName 	= forms.CharField(max_length = 100,required =True)    
		Password 	= forms.CharField(max_length = 100,required =True)
		Email 		= forms.CharField(max_length = 100,required =True)	
		Website 	= forms.CharField(max_length =100,required =True)
		Bio 		= forms.CharField(max_length =300)
		Phone_number = forms.CharField(max_length =100,required =True)
		Gender 		=  forms.ChoiceField(choices=Gender_CHOICES, label="", initial ="" ,widget=forms.Select() ,required =True)   
		Suggestions = forms.BooleanField(False)
		Profile_pic = forms.FileField()

