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
    is_home = True
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
                return render_to_response('index.html', locals(),context_instance= global_context(request))
                 
        else:                       
            print "form not valid"
            invalid_login = session_get(request, "invalid_login")
            form = forms.LoginForm ()
            error_message = "The details provided by you do not match please try again"
    
        
    return render_to_response('index.html', locals(), context_instance= global_context(request))


def display_home(request):
    user = request.user
    if 'logged_in' in request.session and request.session['logged_in'] == True:
        return render_to_response('index.html', locals(), context_instance= global_context(request))
    return HttpResponseRedirect("%slogin/" %(settings.SITE_URL))

@needs_authentication
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


       
@needs_authentication
def updateProfile(request):
    
    #print request.user.username
    #print user
    
    user = request.user
    
    
    if request.method == "POST":
        
        data = request.POST.copy()
        try:    
            form = forms.UpdateProfileForm(data,request.FILES)
        
        except:
            form = forms.UpdateProfileForm(data)
            
        if form.is_valid():
            user.email = form.cleaned_data['email']
            #user.set_password(form.cleaned_data['password'])
            #user.is_active= False
            user.save()
            display_name = form.cleaned_data["display_name"]
            hometown = form.cleaned_data["hometown"]
            skill_set = form.cleaned_data["skill_set"]
            social = form.cleaned_data["social"]
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
       		            about_me = about_me,
       		            hometown = hometown,
       		            skill_set = skill_set,
       		            social = social
                        )
                        
            userprofile.save()
            return HttpResponseRedirect("%smyHome/" %(settings.SITE_URL))
        
        else:
            error = "Please fill the mandatory columns(Name,Roll Number,Branch,Room Number,Email) "
            
            return render_to_response('updateProfile.html', locals(), context_instance= global_context(request))

    else :
        form = forms.UpdateProfileForm()
        error = "These columns are mandatory - (Name,Roll Number, Branch , Room Number , Email)"
        return render_to_response('updateProfile.html', locals(), context_instance= global_context(request))
@needs_authentication
def editProfile(request):
    
    
    
    user = request.user
    profile = UserProfile.objects.get(user__username = user.username)
    if request.method == "POST":
        
        data = request.POST.copy()
        try:    
            form = forms.UpdateProfileForm(data,request.FILES)
        
        except:
            form = forms.UpdateProfileForm(data)
            
        if form.is_valid():
            profile.user.email = form.cleaned_data['email']
            profile.user.save()
            profile.display_name = form.cleaned_data["display_name"]
            profile.hometown = form.cleaned_data["hometown"]
            profile.skill_set = form.cleaned_data["skill_set"]
            profile.social = form.cleaned_data["social"]
            if not form.cleaned_data["photo"] == None:
                profile.photo = form.cleaned_data["photo"]
                       
            if profile.photo == False:
                profile.photo = ""
            profile.room_number = form.cleaned_data["room_number"]
            profile.branch = form.cleaned_data["branch"]
            profile.roll_number = form.cleaned_data["roll_number"]
            profile.mobile_number = form.cleaned_data["mobile_number"]
            
            profile.about_me = form.cleaned_data["about_me"]
            display_edit = True
            
                        
            profile.save()
            return HttpResponseRedirect("%smyHome/" %(settings.SITE_URL))
        
        else:
            error = "Please fill the mandatory columns(Name,Roll Number,Branch,Room Number,Email) "
            
            return render_to_response('editProfile.html', locals(), context_instance= global_context(request))

    
    
    
    
    else:
       
        
        if profile.photo and profile.photo != False:
            form = forms.UpdateProfileForm(initial={'email':profile.user.email,'display_name':profile.display_name,'hometown':profile.hometown,'skill_set':profile.skill_set,'social':profile.social,'room_number':profile.room_number,'branch':profile.branch,'mobile_number':profile.mobile_number,'roll_number':profile.roll_number,'about_me':profile.about_me,'photo':profile.photo})  
        else:
            form = forms.UpdateProfileForm(initial={'email':profile.user.email,'display_name':profile.display_name,'hometown':profile.hometown,'skill_set':profile.skill_set,'social':profile.social,'room_number':profile.room_number,'branch':profile.branch,'mobile_number':profile.mobile_number,'roll_number':profile.roll_number,'about_me':profile.about_me})
                  
            
        error = "These columns are mandatory - (Name,Roll Number, Branch , Room Number , Email)"
        return render_to_response('editProfile.html', locals(), context_instance= global_context(request))

def displayProfile(request,user):

        
                  
        try:
            profile = UserProfile.objects.get(user__username = user)
            print profile
            display_edit = False
        except:
            raise Http404
            
        return render_to_response('profile.html', locals(), context_instance= global_context(request))
        
@needs_authentication
def changePassword(request):
    user = request.user
    profile = UserProfile.objects.get(user__username = user.username)
    display_pass = False
    
    if request.method == "POST":
        
        data = request.POST.copy()
            
        form = forms.changePasswordForm(data)
        
            
        if form.is_valid():
            
            profile.user.set_password(form.cleaned_data['password'])
            #user.is_active= False
            profile.user.save()
            return HttpResponseRedirect("%smyHome/" %(settings.SITE_URL))
        
        else:
            error = "Password(s) too short or dont match"
            
            return render_to_response('changePassword.html', locals(), context_instance= global_context(request))

    
    
    
    
    else:
       
       error = ""
       
       form = forms.changePasswordForm() 
       return render_to_response('changePassword.html', locals(), context_instance= global_context(request))

@needs_authentication
def logout(request):
    request.session['logged_in'] = False
    auth.logout (request)
    return HttpResponseRedirect("%slogin/" %(settings.SITE_URL))

"""
The code below this line is temporarily written to keep everything static.Note later this has to be corrected.

"""    
def alumni(request):
        
    return render_to_response('alumni.html', locals(), context_instance= global_context(request))

def techsoc(request):
    
    
    return render_to_response('techsoc.html', locals(), context_instance= global_context(request))
    

def litsoc(request):
    
    
    return render_to_response('litsoc.html', locals(), context_instance= global_context(request))

def shroeter(request):
    
    
    return render_to_response('shroeter.html', locals(), context_instance= global_context(request))        
"""    
def gallery_hostel(request):
    
    
    return render_to_response('gallery_hostel.html', locals(), context_instance= global_context(request)) 
    
def gallery_inter_hostel(request):
    
    
    return render_to_response('gallery_inter_hostel.html', locals(), context_instance= global_context(request))                                           
    

def gallery_other(request):
        
    return render_to_response('gallery_other.html', locals(), context_instance= global_context(request))                                               
"""    

def contact_secretaries(request):
    
    
    return render_to_response('contact_secretaries.html', locals(), context_instance= global_context(request))                                               
    
    

def contact_warden(request):
    
    
    return render_to_response('contact_warden.html', locals(), context_instance= global_context(request))   
    


def updated_soon(request):
    
    
    return render_to_response('willBeUpdatedSoon.html', locals(), context_instance= global_context(request))       
