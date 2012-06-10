import string
import sys,os

sys.path.append('/home/karthikabinav/django_workspace/AlakanandaHostelWebsite/')
os.environ['DJANGO_SETTINGS_MODULE'] ='Alak.settings'

from django.contrib import auth
from django.contrib.auth.models import User, Group

from django.core.management import setup_environ
from Alak import settings
setup_environ(settings)

from django.template import Context, Template
from Alak.settings import SITE_URL
from Alak.libraryPortal.models import Book


f = open("/home/karthikabinav/django_workspace/AlakanandaHostelWebsite/Alak/misc/books.csv")

N = 6
def insert(line):
    try:
        [sr,name,author] = line.split(',', 3)
    except:
        return
    print sr
    book = Book(name=name,author=author,isVisible=True)
    book.save()
    
for line in f:
    insert(line)

