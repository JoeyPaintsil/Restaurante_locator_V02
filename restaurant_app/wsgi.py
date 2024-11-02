"""
WSGI config for restaurant_app project.

It exposes the WSGI callable as a module-level variable named ``application`` .
wsgi

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/

"""
import collections

# Temporary fix for Python 3.12 compatibility
if not hasattr(collections, 'Sequence'):
    import collections.abc
    collections.Sequence = collections.abc.Sequence


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_app.settings')

application = get_wsgi_application()


app = application