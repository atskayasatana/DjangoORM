import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()
from django.core.management import execute_from_command_line
from django_project.datacenter.models import Passcard, Visit
from django.utils.timezone import localtime
import pytz


if __name__ == "__main__":
 
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
