from django.shortcuts import render , render_to_response
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def login2(request):
	c ={}
	c.update(csrf(request))
	return render_to_response('l.html',c)


def auth_view(request):
	username = request.POST.get('username' , '')
	password = request.POST.get('password' , '')
	user = auth.authenticate(username =username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('register/')
	else:
		return HttpResponseRedirect('register0/')




def register(request):
	if request.method == "POST" :
		 FName = request.POST.get('FName','')
		 UName = request.POST.get('UName','')
		 Password = request.POST.get('Password','')
		 Email = request.POST.get('Email','')	
		 reg_obj = registermodl(Name =FName ,  UserName =UName , Password =Password , Email =Email , Profile_pic = '' , Suggestions = False)	
		 reg_obj.save() 
		 return render_to_response('Login.html',{})
	else:
		return render(request, 'register.html', {})
