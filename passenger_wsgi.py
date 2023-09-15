# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/m/mirodoys/mirodoys.beget.tech/tsm')
sys.path.insert(1, '/home/m/mirodoys/mirodoys.beget.tech/venv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tsm.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
