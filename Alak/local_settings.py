# Please not, any new attributes you want to add to the settings, please add it to the file global_settings.py
# Set the default value in that file and override the value in this file

import global_settings
from global_settings import *

DEBUG = True
ADMINS = (
    ('Karthik Abinav', 'karthikabinavs@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'Alak',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'abc',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '/var/www/Alak/'

SITE_URL = 'http://localhost:8000/'

MEDIA_URL = 'http://localhost/Alak/'


TEMPLATE_DIRS = (
    '/home/karthikabinav/AlakanandaHostelWebsite/Alak/templates/'

)
