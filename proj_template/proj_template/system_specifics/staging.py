import os


PROJ_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GIT_REPO_DIR = os.path.dirname(os.path.dirname(PROJ_DIR))

# staging/qa database
DATABASES = {
    'default': {
        'OPTIONS': {
            'read_default_file': os.path.join(GIT_REPO_DIR, 'staging_db.cnf'),  # out of git
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
        'ENGINE': 'django.db.backends.mysql'
    }
}

DEBUG = False
ALLOWED_HOSTS = []