# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = patterns('',  
       
      (r'^login/?$', 'Alak.home.views.login'),
      (r'^myHome/?$', 'Alak.home.views.Profile'),    
)   


