from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.conf import settings

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
