from django.db import models
from django.contrib.auth.models import User

# the userprofile model.
class UserProfile(models.Model):
    user 			= models.ForeignKey		(User, unique = True)
    display_name    = models.CharField      (max_length = 20) 
    hometown        = models.CharField      (max_length = 100)
    photo           = models.ImageField      (upload_to='profile_pics')
    skill_set       = models.CharField      (max_length = 200)
    social          = models.URLField       ()
    room_number     = models.CharField      (max_length = 10 , default = 'Enter your room number here. e.g. 361B , 359')  
    branch 			= models.CharField		(max_length = 50, default = 'Enter Branch Here', blank = True, null=True, help_text = 'Your branch of study')
    mobile_number 	= models.CharField		(max_length = 15, null=True , help_text='Please enter your current mobile number')
    roll_number 	= models.CharField		(max_length = 40, null=True)
    about_me        = models.CharField      (max_length = 200 , null = True , help_text = ' Write about yourself in less than 200 words ')
    
    def __unicode__(self):
        return self.user.username

    class Admin:
        pass


