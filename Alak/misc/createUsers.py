
import sys,os

sys.path.append('/home/abinav/AlakanandaHostelWebsite/')
os.environ['DJANGO_SETTINGS_MODULE'] ='Alak.settings'

from django.contrib import auth
from django.contrib.auth.models import User, Group

from django.core.management import setup_environ
from Alak import settings
setup_environ(settings)

from django.template import Context, Template
import string,datetime
from Alak.settings import SITE_URL
from Alak.home.models import UserProfile


f = open("/home/abinav/AlakanandaHostelWebsite/users.csv")

N = 6
def insert(line):
    [username,password,email] = line.split(',', 3)
    name = username.replace('&', '').replace('!', '').replace('\'', '').replace('-', '').replace('  ', '')#removing most commonly used special characters
    user = User.objects.create_user(username = name,password = password,email = email,)
    user.is_active = False
    user.is_staff = False
    user.is_super_user=False
    user.last_login = datetime.datetime.now()
    user.date_joined = datetime.datetime.now()
    
    user.save()
    
for line in f:
    insert(line)


print "success"
        
        
    
