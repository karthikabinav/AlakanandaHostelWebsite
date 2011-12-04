# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = patterns('',  
       
      (r'^login/?$', 'Alak.home.views.login'),
      (r'^UpdateProfile/?$', 'Alak.home.views.updateProfile'),
      (r'^EditProfile/?$', 'Alak.home.views.editProfile'),
      (r'^myHome/?$', 'Alak.home.views.Profile'),
      (r'^changePassword/?$', 'Alak.home.views.changePassword'),
      (r'^logout/?$', 'Alak.home.views.logout'),
      (r'^residents/(?P<user>.*)/?$', 'Alak.home.views.displayProfile'),        
)   



