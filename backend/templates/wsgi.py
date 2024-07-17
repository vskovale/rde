#!/usr/bin/env python
import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/rde')
sys.path.append('/var/www/rde/rde')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rde.settings')

application = get_wsgi_application()
