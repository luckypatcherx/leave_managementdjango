"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys
#add your project directory

project_home= '/home/abhiramtn/leave_managementdjango'
if project_home not in sys.path:
    sys.path.insert(0,project_home)




#set environment variable to tell django where your serttings.py file is
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
