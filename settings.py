DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'users',
        'USER': 'cfortunylombra',
        'PASSWORD': 'cfl22ca',
        'HOST': 'localhost',
        'PORT': '',
    }
}

