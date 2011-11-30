from django import forms
from django.forms import ModelForm
from django.db import models as d_models
import re 
from django.contrib.auth.models import User
from django.template import Template, Context
from django.utils.safestring import mark_safe

from Alak.home import models
from Alak import settings
 
alnum_re = re.compile(r'^[\w.-]+$') # regexp. from jamesodo in #django  [a-zA-Z0-9_.]
alphanumric = re.compile(r"[a-zA-Z0-9]+$")
            
class LoginForm(forms.Form):
    username=forms.CharField(help_text='The username you were provided with')
    password=forms.CharField(widget=forms.PasswordInput, help_text='Your password')
    

