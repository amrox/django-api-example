from settings_base import *

# database settings are injected by heroku automatically

# DON'T ACTUALLY SHIP WITH THESE SETTINGS
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATIC_URL = "/static/"
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

SERVE_MEDIA = DEBUG
