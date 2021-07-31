
from django.conf import settings
settings.configure()
import django
django.setup()
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from MKsystemApp.models import Exchange

if __name__ == '__main__':
    echange = Exchange("", "")
    echange.save()
