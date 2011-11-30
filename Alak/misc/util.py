# Helper functions
from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template.context import Context, RequestContext

from Alak import settings
from Alak.home.models import *
import Alak
#from main_test.users import models
import datetime
import MySQLdb
import re, md5, time


# Generates a context with the most used variables
def global_context(request):
  
    context =  RequestContext (request,{'MEDIA_URL':settings.MEDIA_URL ,'user' : request.user,},  )
            
    return context


# Convert Foo Contest <-> FooContest
def camelize (str):
    return str.replace(' ','').replace('!', '').replace('&', '').replace("'", '').replace('-', '')

def decamelize (str):
    p = re.compile (r'([A-Z][a-z]*)')
    result = ''
    for blob in p.split (str):
        if blob != '':
            result += blob + ' '
    return result[:-1]

# Take care of session variable
def session_get (request, key, default=False):
    value = request.session.get (key, False)
    if value:
        pass
        del request.session[key]
    else: 
        value = default
    return value


            


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

# Check for coords status. Use *after* needs_authentication. Always
def coords_only (func):
    def wrapper (*__args, **__kwargs):
        request = __args[0]
        userprofile= request.user.get_profile()
        if userprofile.is_coord == True:
            return func (*__args, **__kwargs)
        else:
            request.session['access_denied'] = True
            return HttpResponseRedirect ("%shome/"%settings.SITE_URL)
    return wrapper

# Check for eventcore status. Use *after* needs_authentication. Always
def event_cores_only (func):
    def wrapper (*__args, **__kwargs):
        request = __args[0]
        if request.user.groups.filter(name="EventCores"):
            return func (*__args, **__kwargs)
        else:
            request.session['access_denied'] = True
            return HttpResponseRedirect ("%s/home/"%settings.SITE_URL)
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
