#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
from django.core.management import execute_from_command_line
from django_project.datacenter.models import Passcard, Visit
from django.utils.timezone import localtime
import pytz

execute_from_command_line('manage.py runserver'.split())


