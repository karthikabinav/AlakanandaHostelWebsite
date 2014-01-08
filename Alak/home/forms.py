from django import forms
from django.db import models 
from django.contrib.auth.models import User
from django.template import Template, Context

from Alak.home import models
            
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = models.AddUsers


class changePasswordForm(forms.Form):
    
    password = forms.CharField  (min_length=6,
                                       max_length=30,
                                       widget=forms.PasswordInput,
                                       )
    password_again = forms.CharField  (max_length=30,
                                       widget=forms.PasswordInput,
                                       
                                       ) 
    
    
    def clean_password(self):
        if self.prefix:
            field_name1 = '%s-password' % self.prefix
            field_name2 = '%s-password_again' % self.prefix
        else:
            field_name1 = 'password'
            field_name2 = 'password_again'
            
        if self.data[field_name1] != '' and self.data[field_name1] != self.data[field_name2]:
            raise forms.ValidationError ("The entered passwords do not match.")
        else:
            return self.data[field_name1]
    
class UpdateProfileForm(forms.Form):
    
    
    email = forms.EmailField ()
    display_name = forms.CharField()
    hometown = forms.CharField(required=False)
    skill_set = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 7}), max_length=200, required=False)
    social = forms.URLField(required=False)
    photo = forms.ImageField(required=False,)
    room_number = forms.CharField()
    branch = forms.CharField()
    roll_number = forms.CharField()
    mobile_number = forms.CharField(required=False)
    about_me = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 8}), max_length=200, required=False)
    
    class Meta:
        model = models.UserProfile
        fields = ('display_name', 'password', 'password_again', 'photo', 'roll_number', 'branch', 'hometown', 'about_me', 'skill_set', 'phone_number', 'room_number', 'email', 'facebook')
        
    def clean_name(self):
	if not self.cleaned_data['name'].replace(' ', '').isalpha():
	    raise forms.ValidationError(u'Names cannot contain anything other than alphabets.')
	else:
	    return self.cleaned_data['name']
	  
    
    def clean_email(self):
        return self.cleaned_data['email']
        

    
