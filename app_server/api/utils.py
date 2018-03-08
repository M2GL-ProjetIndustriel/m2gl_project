from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def init_tokens():
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
