from django.urls import path,re_path,include
from django.contrib import admin
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from .views import complaint_create, complaint_detail, complaint_list,complaint_update,fir_create,copstatus_create,casestatus_create,login,caseclose
from django.contrib.auth import views as auth_views

app_name='crimefiles'
urlpatterns = [
    re_path(r'^login/',auth_views.login,name='login',kwargs={'template_name': 'login_form.html'}),
	re_path(r'^createcomplaint$',complaint_create),
	re_path(r'^(?P<id>\d+)/createfir$',fir_create),
	re_path(r'^(?P<id>\d+)/createcopstatus$',copstatus_create),
	re_path(r'^(?P<id>\d+)/createcasestatus$',casestatus_create),
	re_path(r'^(?P<id>\d+)/closecase$',caseclose),
	path('', complaint_list,name="list"),
	re_path(r'^(?P<id>\d+)/edit$', complaint_update,name="update"),
	re_path(r'^(?P<id>\d+)/$', complaint_detail,name="detail"),



	]
