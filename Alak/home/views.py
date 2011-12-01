from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.template.loader import get_template
from django.template.context import Context, RequestContext
from django.utils.translation import ugettext as _
from django.core.mail import send_mail,EmailMessage,SMTPConnection
from django.contrib.sessions.models import Session
from django.utils import simplejson

from Alak.misc.util import *
from Alak.settings import *
from Alak.home.models import *
from Alak.home import forms
import sha,random,datetime

def login (request):
       
    form=forms.LoginForm()
    if 'logged_in' in request.session and request.session['logged_in'] == True:
	    return HttpResponseRedirect("%smyHome/" % settings.SITE_URL)	            
            
    if request.method == 'POST':
        data = request.POST.copy()
        form = forms.LoginForm(data)
        if form.is_valid():
            print "form is valid"
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data["password"])
            if user is not None:
                auth.login (request, user)
                request.session['logged_in'] = True
                #try:
                print "mama" + user.username
                return HttpResponseRedirect("%smyHome/" %(settings.SITE_URL))
                #except:
                    #return HttpResponseRedirect("%s" % settings.SITE_URL)        
            else:
                
                request.session['invalid_login'] = True
                request.session['logged_in'] = False
                errors=[]
                errors.append("Incorrect username and password combination!")
                return render_to_response('login.html', locals(),context_instance= global_context(request))
                 
        else:                       
            print "form not valid"
            invalid_login = session_get(request, "invalid_login")
            form = forms.LoginForm ()
            error_message = "The details provided by you do not match please try again"
    return render_to_response('login.html', locals(), context_instance= global_context(request))


def Profile(request):

        
        
        
        #print correct_user == user
        #print request.session['logged_in']
        
        user = request.user
        try:
            profile = UserProfile.objects.get(user__username = user.username)
            #name = profile.display_name
            
            display_edit = True
        except:
            
            return HttpResponseRedirect("%sUpdateProfile/" %(settings.SITE_URL))
        
        
        return render_to_response('profile.html', locals(), context_instance= global_context(request))
    
        

def updateProfile(request):
    
    #print request.user.username
    #print user
    
    user = request.user
    
    if request.method == "POST":
        data = request.POST.copy()
        form = forms.UpdateProfileForm(data)
        
        if form.is_valid():
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password'])
            user.is_active= False
            user.save()
            display_name = form.cleaned_data["display_name"]
            photo = form.cleaned_data["photo"]
            room_number = form.cleaned_data["room_number"]
            branch = form.cleaned_data["branch"]
            roll_number = form.cleaned_data["roll_number"]
            mobile_number = form.cleaned_data["mobile_number"]
            
            about_me = form.cleaned_data["about_me"]
            display_edit = True
            
            userprofile = UserProfile(
                        user = user,
                        mobile_number = mobile_number,
       		            display_name  = display_name,
       		            photo = photo,
       		            room_number = room_number,
       		            branch = branch,
       		            roll_number = roll_number,
       		            about_me = about_me
                        )
                        
            userprofile.save()
            return HttpResponseRedirect("%smyHome/" %(settings.SITE_URL))
        
        else:
            error = "Please fill the mandatory columns "
            
            return render_to_response('updateProfile.html', locals(), context_instance= global_context(request))

    else :
        form = forms.UpdateProfileForm()
        return render_to_response('updateProfile.html', locals(), context_instance= global_context(request))



def displayProfile(request,user):

              
        try:
            profile = UserProfile.objects.get(user__username = user)
            print profile
            display_edit = False
        except:
            raise Http404
            
        return render_to_response('profile.html', locals(), context_instance= global_context(request))
