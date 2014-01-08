# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = patterns('',  
      (r'^/?$', 'Alak.home.views.display_home'), 
      (r'^login/?$', 'Alak.home.views.login'),
      (r'^UpdateProfile/?$', 'Alak.home.views.updateProfile'),
      (r'^EditProfile/?$', 'Alak.home.views.editProfile'),
      (r'^myHome/?$', 'Alak.home.views.Profile'),
      (r'^changePassword/?$', 'Alak.home.views.changePassword'),
      (r'^logout/?$', 'Alak.home.views.logout'),
      (r'^alumni/?$', 'Alak.home.views.alumni'),
      (r'^activities/techsoc/?$', 'Alak.home.views.techsoc'),
      (r'^activities/litsoc/?$', 'Alak.home.views.litsoc'),
      (r'^activities/shroeter/?$', 'Alak.home.views.shroeter'),
      (r'^gallery/hostel/?$', 'Alak.home.views.updated_soon'),
      (r'^gallery/inter-hostel/?$', 'Alak.home.views.updated_soon'),
      (r'^gallery/other/?$', 'Alak.home.views.updated_soon'),
      (r'^contact/secretaries/?$', 'Alak.home.views.contact_secretaries'),
      (r'^contact/warden/?$', 'Alak.home.views.contact_warden'),
      (r'^willBeUpdatedSoon/?$', 'Alak.home.views.updated_soon'),
      (r'^qwerThisasdfISzxcvPASSWORD/?$', 'Alak.home.views.CreateUsers'),
      (r'^residents/(?P<user>.*)/?$', 'Alak.home.views.displayProfile'),        
)   



