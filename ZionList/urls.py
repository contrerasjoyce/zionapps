from ContrerasList import views
from django.urls import include, re_path
from django.contrib import admin
from django.urls import re_path as path

urlpatterns = [  
    path('admin/', admin.site.urls),    
    path(r'^$', views.Homerun, name='Homerun'),    
    path(r'^Home$', views.Home, name='Home'),
    path(r'^require$', views.require, name='require'),
    path(r'^Offered$', views.Offered, name='Offered'),
    path(r'^Contact$', views.Contact, name='Contact'),   
    path(r'^adminlogin$', views.adminlogin, name='adminlogin'),
    path(r'^List$', views.List, name='List'),
    path(r'^View$', views.View, name='View'),
    path(r'^AdminHome$', views.AdminHome, name='AdminHome'),
    path(r'^Homerun_Form$', views.Homerun_Form, name='Homerun_Form'), 
    path(r'^new$', views.new_applicant, name='new_applicant'),    
    path(r'^(\d+)/view_applicant$', views.view_applicant, name='view_applicant'),   
    path(r'^(\d+)/add_applicant$', views.add_applicant, name='add_applicant'),
    

    path(r'^adminaccount$', views.adminaccount, name='adminaccount'),  
    path(r'^applicant_list$', views.applicant_list, name='applicant_list'), 
    path(r'^(\d+)/applicant_view$', views.applicant_view, name='applicant_view'), 

    path(r'^applicant_page$', views.applicant_page, name='applicant_page'), 
    path(r'^admin_page$', views.admin_page, name='admin_page'), 

    path(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    path(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    path(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),]