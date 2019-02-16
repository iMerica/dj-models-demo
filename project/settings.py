SECRET_KEY = '<ACTUAL SECRET KEY>'
DATABASES = {
    'default': {
        'ENGINE': 'djmodels.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'db',
        'PORT': '5432',
    }
}

INSTALLED_APPS = ['project.base']
