from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()

file = open('.env', 'a')
file.write('SECRET_KEY = '+SECRET_KEY)
file.close()
    
