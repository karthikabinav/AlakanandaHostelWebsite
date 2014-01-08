from django.db import models
from django.contrib.auth.models import User
import os

# the userprofile model.
class UserProfile(models.Model):
    user 			 = models.ForeignKey		(User, unique=True)
    display_name = models.CharField      (max_length=20) 
    hometown = models.CharField      (max_length=100)
    photo = models.ImageField      (upload_to='profile_pics')
    
    skill_set = models.CharField      (max_length=200)
    social = models.URLField       ()
    room_number = models.CharField      (max_length=10 , default='Enter your room number here. e.g. 361B , 359')  
    branch 			 = models.CharField		(max_length=50, default='Enter Branch Here', blank=True, null=True, help_text='Your branch of study')
    mobile_number 	 = models.CharField		(max_length=15, null=True , help_text='Please enter your current mobile number')
    roll_number 	 = models.CharField		(max_length=40, null=True)
    about_me = models.CharField      (max_length=200 , null=True , help_text=' Write about yourself in less than 200 words ')
    
    def __unicode__(self):
        return self.user.username


    __original_image = None
    
    def __init__(self, *args, **kwargs):
        super(UserProfile, self).__init__(*args, **kwargs)
        self.__original_image = self.photo
    
    def save(self, force_insert=False, force_update=False):
        if self.photo != self.__original_image and self.__original_image != '':
            self.delete_images()
 
        super(UserProfile, self).save(force_insert, force_update)
        self.__original_image = self.photo    
    
    
    def delete_images(self, empty_image=False):
        image_path = os.path.join(settings.MEDIA_ROOT, str(self.__original_image))
 
        try:
            os.remove(image_path)
            self.main_image.delete()
        except:
            pass
 
        if empty_image:
            self.photo = ''
    
    class Admin:
        pass

class AddUsers(models.Model):
    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    class Admin:
        pass
