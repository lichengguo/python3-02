"""
Django settings for djangodemo project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 定义变量  获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# 秘钥
# hashlin.md5("用户原文密码"+"秘钥")
SECRET_KEY = 'ihzo2q=h+tt^s6m37ndd@&exzb#87y_5i4584-n@_5oo=f#9x3'

# SECURITY WARNING: don't run with debug turned on in production!
# 项目上线时,设置DEBUG=True,同时配置ALLOWED_HOSTS
DEBUG = True
# 设置允许通过哪些地址可以访问到django项目
ALLOWED_HOSTS = []



# Application definition
# 子应用注册列表
INSTALLED_APPS = [
    'django.contrib.admin', # admin站点管理后台
    'django.contrib.auth',  # 用户认证模块
    'django.contrib.contenttypes',  # 数据库的关系管理
    'django.contrib.sessions',      # session模块
    'django.contrib.messages',      # 消息模块[针对错误提示，运行提醒]
    'django.contrib.staticfiles',   # 静态文件管理[ css/js/html ]
    'students',
    'users',
    'stusys',
]

# 中间件/全局钩子:
# 应用场景：加密，安全监测，session,csrf，权限,消息读取

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # csrf拦截
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'djangodemo.middlewares.simple_middleware1',
    'djangodemo.middlewares.simple_middleware2',
]
# 设置总路由路径
ROOT_URLCONF = 'djangodemo.urls'

# 模板引擎的相关配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # "D:/yuan/周末2期/djangodemo/templates", # 错误写法，
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# web服务器实现的核心类
WSGI_APPLICATION = 'djangodemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
# 数据库配置
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "djangodemo",
        'HOST':"localhost",
        'PORT':3306,
        "USER":"root",
        "PASSWORD":"123456",
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
# 密码验证功能
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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
# 本地化与国际化
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'
# 时区
TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# 静态文件的相关配置
# 访问静态文件的地址前缀
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statcis"),
]
