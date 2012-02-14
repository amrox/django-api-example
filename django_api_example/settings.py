import os
from settings_base import *

# (production, staging, development, local)
deploy_config = os.getenv('DEPLOY_CONFIG')

if deploy_config == 'production':
    from settings_production import *
else:
    from settings_local import *
