from django.shortcuts import render , render_to_response
from .models import registermodl , timelinemodl , friendmodl
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadForm , Edit_form , TimeLinePostForm,RegistrationForm
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q
import random
from operator import attrgetter
from django.contrib import auth
from django.core.context_processors import csrf



# redirect to login page.
try:
	def login2(request):
			c ={}
			c.update(csrf(request))
			return render_to_response('l.html',c)
except Exception as e:
	print e


	


def register(request):	
		form = RegistrationForm()
		return render_to_response('UserRegister.html', {'form':form})


# redirect to main page
try:
	def login(request):
		if request.method == "POST":
			lst =[] #store data about all friends of user
			lst2 =[] # store data about user's frind's POST
			lst3 = [] # store data about user(already in friends list and people who has send friend request to logged in user)
			username = request.POST.get('name','')
			password = request.POST.get('pw','')
			user_id0 = registermodl.objects.filter(UserName = username).filter(Password = password).all()
			for h in user_id0:
				user_ID = h.id
			request.session['ses_key'] = user_ID
			
			"""user is userID fetched from register model(registermodl)
			   Now, using that data and filter() I have display friend suggestion to follow on main page
			   """
			frnd = friendmodl.objects.filter(User_No = user_ID).filter(Friend_status = True).all()
			frnd2 = friendmodl.objects.filter(User_No = user_ID).filter(Request_status = True).all()		
			for i in frnd:
				lst.append(i.Friend_No)
				lst3.append(i.Friend_No)
			lst3.append(user_ID)
			for o in frnd2:
				lst3.append(o.Friend_No)
			m =registermodl.objects.filter(~Q(pk__in = lst3))

			""" timelinemodl(this contains each user's posted data) 
			    Getting data of user's friends's POST """

			POST0_DATA = registermodl.objects.filter(pk__in=lst)
			for g in POST0_DATA:
				for j in g.timelinemodl_set.all():
					lst2.append(j)	

			# for uploading profile pic
			form = ImageUploadForm()			

			return render_to_response('Main.html',{'user_data':user_id0.all(), 'form':form,'friends':random.sample(m,3),'POST_DATA':sorted(lst2,key = attrgetter('Post_time'),reverse=True)} ) 	
		else:
			return render(request, 'Login.html', {})
except Exception as e:
	print e

# upload profile picture
@csrf_exempt
def upload_pic(request ):		
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES or None)
       	obj1 = request.session['ses_key']
      	m = registermodl.objects.get(pk = obj1)
       	Profile_pic0 = request.FILES['id_image']
       	m.Profile_pic = Profile_pic0
       	m.save()
   	return render_to_response('Main.html',{'user_data':registermodl.objects.filter(id = obj1)})



@csrf_exempt
def MyProfile(request):
	 if request.method=='GET':
         	profile = request.GET.get('profile')
         	if not profile:
    			return render_to_response('Main.html',{'user_data':registermodl.objects.filter(id = obj1)})
         	else: 
        		 form = TimeLinePostForm()        
           		 return render(request, 'Myprofile.html' , {'user_post':timelinemodl.objects.filter(id = profile),'MyProfile':registermodl.objects.filter(id = profile) , 'form':form})


@csrf_exempt
def Edit_Profile(request):
	if request.method == "POST":	
		form = Edit_form()
		profile = request.POST.get('user_icon')
        return render(request, 'Edit_Profile.html' , {'MyProfile':registermodl.objects.filter(id = profile) , 'form':form})

@csrf_exempt
def Edit_data(request):
	if request.method == "POST":
		form = Edit_form(request.POST)
		if form.is_valid():
			val = request.POST.get('link_user')
			m = registermodl.objects.get(pk = val)
			m.Name = request.POST.get('Name','')
			m.UserName = request.POST.get('UserName','')
			m.Website = request.POST.get('Website','')
			m.Bio = request.POST.get('Bio','')
			m.Email = request.POST.get('Email','')
			m.Phone_number = request.POST.get('Phone_number','')
			m.Gender = request.POST.get('Gender','')
			m.Suggestions  = request.POST.get('Suggestions','')
			m.save()
		return render_to_response('MyProfile.html',{'MyProfile':registermodl.objects.filter(id = val)})


def My_post(request):
	if request.method =="POST":
		icon = request.POST.get('user_ic')
		form = TimeLinePostForm(request.POST, request.FILES or None)
       	obj1 = request.session['ses_key']
      	m = registermodl.objects.get(pk = obj1)
      	post = request.POST.get('Name')
      	post_pic = request.FILES['post_image']
      	post_obj = timelinemodl(PostNo = m , Post = post, Post_pic = post_pic)
      	post_obj.save()
     	return render (request , 'MyProfile.html',{'MyProfile':registermodl.objects.filter(id=icon)})

@csrf_exempt
def friend_request(request):
	if request.method == "POST":
		User_No = request.POST.get('User_No')
		Friend = request.POST.get('Friend')
		friendmodl.objects.create(

			User_No = User_No , 
			Friend_No = Friend ,
			Request_status = True ,
			Friend_status =False,
		)	
		return HttpResponse('')

@csrf_exempt
def Sug_list(request):
	if request.method=='GET':
        	sug = request.GET.get('sug')
        	lst =[]
        	yeah = friendmodl.objects.filter(User_No=sug).filter(Request_status = True).all()
        	yeah2 = friendmodl.objects.filter(User_No = sug).filter(Friend_status = True).all()
        	for i in yeah2:
				lst.append(i.Friend_No)
	    	for y in yeah:
				lst.append(y.Friend_No)

	    	o = registermodl.objects.filter(~Q(id =sug))
	    	m = o.filter(~Q(pk__in = lst))
	return render(request,'Friend_Sug.html',{'user_data':registermodl.objects.filter(id = sug),'friends':m})

@csrf_exempt
def friend_profile(request):
	if request.method == "GET":
		myid = request.GET.get('myid')
		urid = request.GET.get('urid')
		return render(request,'Friend_profile.html',{'friend_data':registermodl.objects.filter(id = urid),'my_data':registermodl.objects.filter(id=myid)})

def Notifications(request):
	if request.method == "GET":
		lst=[]
		myid= request.GET.get('myid')
		print myid
		req = friendmodl.objects.filter(Friend_No = myid).filter(Request_status =True).all()
		for o in req:
			lst.append(o.User_No)
		user = registermodl.objects.filter(pk__in=lst)
		return render(request,'Notification.html',{'req':user,'my_data':registermodl.objects.filter(id=myid)})

@csrf_exempt
def accept_req(request):
	if request.method == "POST":
		user = request.POST.get('user')
		frnd = request.POST.get('frnd')
		accept = request.POST.get('accept')
		print "FRND"+ frnd
		if accept == 'Accept':
			friendmodl.objects.filter(User_No = frnd).filter(Friend_No = user).update(User_No = frnd,Friend_No = user,Request_status = False,Friend_status = True)
			friendmodl.objects.create(
				User_No = user,
				Friend_No = frnd,
				Request_status = False,
				Friend_status = True,
			)
			return HttpResponse('')


@csrf_exempt
def decline_req(request):
	if request.method == "POST":
		user = request.POST.get('user')
		frnd = request.POST.get('frnd')
		Decline = request.POST.get('Decline')
		print "USER"+user 		
		if Decline == "Decline":
			friendmodl.objects.filter(User_No = frnd).filter(Friend_No = user).delete()				
			return HttpResponse('')