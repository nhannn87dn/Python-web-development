"""
Django settings for bikestore project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import dj_database_url
import os
from pathlib import Path

# Add by nhannn87dn
APP_MODE = os.getenv('APP_MODE', 'development')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7b$f#@)jrvbti6u4*2-_a&4$rx)*+dpld-6-x@xl$#)7z=8&(0'

# SECURITY WARNING: don't run with debug turned on in production!

if APP_MODE == 'production':
    # Production Mode
    DEBUG = False
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = True
    ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ## Bootstrap
    'bootstrap5',
    'fontawesomefree',
    ## app your self
    'cart',
    'home',
    'staff',
    'category',
    'brand',
    'product',
    'customer',
    'order',
    ## ckeditor
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #static
    'customer.middleware.CustomerAuthMiddleware', # customers
]

ROOT_URLCONF = 'bikestore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #Cấu hình templates chung cho các app
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # Thêm dòng này để tạo biến global cho giỏ hàng trên Header
                'cart.context_processors.cart_item_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'bikestore.wsgi.application'


# SEND EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 # 465
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ecshopvietnamese@gmail.com'
EMAIL_HOST_PASSWORD = 'bhvksgtrvzrsukqk'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Lựa chọn Database dự vào biến môi trường

if APP_MODE == 'development':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "BikeStoresDjango",
            "USER": "postgres",
            "PASSWORD": "123456789",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
elif APP_MODE == 'production':
    DATABASES = {
    "default": dj_database_url.parse('postgres://bikestoredjango_user:4OoSjAq1q3qWKlHWuBPADiPQmSoXz1gB@dpg-cnu072nsc6pc7392huf0-a.singapore-postgres.render.com/bikestoredjango')
}
#DATABASES = {
    
    # "default": dj_database_url.parse('postgres://bikestoredjango_user:4OoSjAq1q3qWKlHWuBPADiPQmSoXz1gB@dpg-cnu072nsc6pc7392huf0-a.singapore-postgres.render.com/bikestoredjango')
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": "BikeStoresDjango",
    #     "USER": "postgres",
    #     "PASSWORD": "123456789",
    #     "HOST": "localhost",
    #     "PORT": "5432",
    # }
#}

#Chỉ định lại Model xác thực cho Django
AUTH_USER_MODEL = 'staff.Staff'

CUSTOMER_LOGIN_URL = '/customer/login'

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default backend for Staff
    'customer.auth_backends.CustomerAuthBackend',  # Custom backend for Customer
]
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/' #đường dẫn tương đối đến static

#Đây là thư mục mà python manage.py collectstatic sẽ thu thập tất cả các tệp tĩnh vào. 
#Bạn nên đặt nó thành một đường dẫn tuyệt đối
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Đây là danh sách các thư mục mà Django sẽ tìm kiếm tệp tĩnh. 
# Đây phải là các đường dẫn tuyệt đối
STATICFILES_DIRS = [
    BASE_DIR / 'assets/static',
    # Thêm thêm thư mục static toàn cục khác nếu cần
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#Đường dẫn URL để truy cập đến tập tin
MEDIA_URL = '/assets/media/uploads/'
# Đường dẫn tuyệt đối để upload tập tin
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets/media/uploads/')

#Ckeditor
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_CONFIGS = {
    'default': {
        #'skin': 'office2013', #moono | office2013
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            
            '/',
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image',  'Table',  'Smiley']},
            '/',
            {'name': 'styles', 'items': ['Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks','Source']},
            
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
    }
}



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cấu hình xem Log hệ thống --> có tạo file debug.log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        # Log riêng cho customer view
        'customer.views': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}