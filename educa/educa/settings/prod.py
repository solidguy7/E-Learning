from .base import *

DEBUG = False

ADMINS = [
    ('solidguy7', ''),
]

ALLOWED_HOSTS = ['myeducaproject.com', 'www.myeducaproject.com']

REDIS_URL = 'redis://redis:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
