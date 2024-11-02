"""
WSGI config for restaurant_app project.

It exposes the WSGI callable as a module-level variable named ``application`` .
wsgi

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/

"""

import os
from collections.abc import Sequence, Mapping  # Directly import from collections.abc

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_app.settings')

application = get_wsgi_application()
app = application
