from .base import *

DEBUG = False

ADMINS = [
    ('solidguy7', ''),
]

ALLOWED_HOSTS = ['*']

REDIS_URL = 'redis://redis:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]
