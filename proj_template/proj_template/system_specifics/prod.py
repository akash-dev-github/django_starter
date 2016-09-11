import os
from staging import *


# staging/qa database
DATABASES = {
    'default': {
        'OPTIONS': {
            'read_default_file': os.path.join(GIT_REPO_DIR, 'prod_db.cnf'),  # out of git
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
        'ENGINE': 'django.db.backends.mysql'
    }
}
