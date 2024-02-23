from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

def generar_token():
    return uuid.uuid4().hex  # Genera un token UUID único

class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    token_user= models.CharField(max_length=100, default=generar_token)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    def save(self, *args, **kwargs):
        if not self.token_user:
            self.token_user = generar_token()
        super().save(*args, **kwargs)