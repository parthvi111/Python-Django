from django.conf.urls import url
from django.contrib import admin
from . import views



urlpatterns = [

	url(r'^$',views.login2),
	url(r'^register/$',views.register),
	url(r'^login1/$',views.login),
	url(r'^login1/Sug_list/$',views.Sug_list),
	url(r'^login1/Notifications/$',views.Notifications),
	url(r'^login1/Sug_list/friend_profile/$',views.friend_profile),
	url(r'^login1/friend_profile/$',views.friend_profile),
	url(r'^login1/friend_request/$',views.friend_request),
	url(r'^login1/upload_pic/$' , views.upload_pic),
	url(r'^login1/MyProfile/$',views.MyProfile),
	url(r'^login1/MyProfile/Edit_Profile/$',views.Edit_Profile),
	url(r'^login1/MyProfile/Edit_Profile/Edit_data/$',views.Edit_data),
	url(r'^login1/MyProfile/My_post/$',views.My_post),
	url(r'^login1/friend_request/friend_request/$',views.friend_request),
	url(r'^login1/friend_request/friend_request/friend_request/$',views.friend_request),
	url(r'^login1/Notifications/accept_req/$',views.accept_req),
	url(r'^login1/Notifications/decline_req/$',views.decline_req),

	url(r'^login1/friend_request/friend_request/friend_request/$',views.friend_request),




	
]
