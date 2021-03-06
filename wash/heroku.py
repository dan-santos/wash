import environ

from .settings import *

env = environ.Env()

# Criando variaveis de ambiente

DEBUG = env.bool('DEBUG', False)

SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', True)

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}