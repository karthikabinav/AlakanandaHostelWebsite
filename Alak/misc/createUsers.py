import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys,os

sys.path.append('/home/alakanan/test/Alak/AlakanandaHostelWebsite/')
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


f = open("/home/alakanan/test/Alak/AlakanandaHostelWebsite/Alak/users.csv")

N = 6
def insert(line):
    [room,roll,username] = line.split(',', 3)
    name = username.lower().replace(' ','').replace('\n','')
    
    password = ''.join(random.sample(string.ascii_lowercase + string.digits,7))
    email = roll.lower() + "@smail.iitm.ac.in"
	
    user = User.objects.create_user(username = name,password = password,email = email,)
    user.is_active = True
    user.is_staff = True
    user.is_super_user=False
    user.last_login = datetime.datetime.now()
    user.date_joined = datetime.datetime.now()
    
    user.save()
    
    me = "noreply.alakananda@gmail.com"
    you = email

	msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alak username and password"
    msg['From'] = me
    msg['To'] = you

    text = "Username = " + name + "\nPassword = " + password +"\nemail = " + email
    html = "<html><body><p>username = "+name+" <br>Password = "+password+"\nemail = "+email+"</p></body></html>"
	

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
	
    msg.attach(part1)
    msg.attach(part2)

    gmail_user = 'noreply.alakananda@gmail.com'
    gmail_pwd = '<insert correct pass here>'
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    smtpserver.sendmail(me, you, msg.as_string())
    smtpserver.quit()

    
for line in f:
    insert(line)

