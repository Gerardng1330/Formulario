# serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ValidationToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ValidationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationToken
        fields = ('user', 'token')
