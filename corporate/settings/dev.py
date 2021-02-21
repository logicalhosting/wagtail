from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o_8hr*jup^195jqxd!-liwi+m69bn2bf&i4f)6$!a99vav4bp4'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['192.168.1.45', '10.206.56.220', 'localhost'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
