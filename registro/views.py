# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import ValidationToken
from .serializers import UserSerializer, ValidationTokenSerializer
from django.contrib.auth.tokens import default_token_generator

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generar y guardar el token de validación
        token = default_token_generator.make_token(user)
        ValidationToken.objects.create(user=user, token=token)

        return Response({'detail': 'Usuario registrado exitosamente.'}, status=status.HTTP_201_CREATED)

class UserValidationView(generics.UpdateAPIView):
    serializer_class = ValidationTokenSerializer
    queryset = ValidationToken.objects.all()

    def update(self, request, *args, **kwargs):
        token = kwargs.get('token')
        try:
            validation_token = ValidationToken.objects.get(token=token)
            user = validation_token.user
            user.is_active = True
            user.save()
            validation_token.delete()
            return Response({'detail': 'Usuario validado exitosamente.'}, status=status.HTTP_200_OK)
        except ValidationToken.DoesNotExist:
            return Response({'detail': 'Token de validación no válido.'}, status=status.HTTP_400_BAD_REQUEST)
