# Helper functions
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template.context import Context, RequestContext

from django.conf import settings
from Alak.home.models import *
import Alak
#from main_test.users import models
import datetime
import MySQLdb
import re, md5, time


# Generates a context with the most used variables
def global_context(request):
  
    context =  RequestContext (request,{'MEDIA_URL':settings.MEDIA_URL ,'STATIC_URL':settings.STATIC_URL,'user' : request.user,'is_home':False,'display_pass':True},  )
            
    return context

# Decorators

# Force authentication first
def needs_authentication (func):
    def wrapper (*__args, **__kwargs):
        request = __args[0]
        if not request.user.is_authenticated():
            # Return here after logging in
            request.session['from_url'] = request.get_full_path()
            return HttpResponseRedirect ("%slogin/"%settings.SITE_URL)
        else:
            return func (*__args, **__kwargs)
    return wrapper

# Check for admin status. Use *after* needs_authentication. Always
def admin_only (func):
    def wrapper (*__args, **__kwargs):
        request = __args[0]
        if request.user.is_superuser:
            return func (*__args, **__kwargs)
        else:
            request.session['access_denied'] = True
            return HttpResponseRedirect ("%s/home/"%settings.SITE_URL)
    return wrapper

# For urls that can't be accessed once logged in.
def no_login (func):
    def wrapper (*__args, **__kwargs):
        request = __args[0]
        if request.user.is_authenticated():
            # Return here after logging in
            request.session['already_logged'] = True
	    #html = "%s/home/" %SITEURL
            return HttpResponseRedirect ("%s/home/" %settings.SITE_URL)
        else:
            return func (*__args, **__kwargs)
    return wrapper
