from settings_base import *
import posixpath

# database settings are injected by heroku automatically

# Debug Media serving settings
#
# DON'T ACTUALLY SHIP WITH THESE SETTINGS
# 

STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "/static/"
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

DEBUG = False
SERVE_MEDIA = DEBUG

DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            }
        }
