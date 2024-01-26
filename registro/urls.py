# urls.py

from django.urls import path
from .views import UserRegistrationView, UserValidationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('validate/<str:token>/', UserValidationView.as_view(), name='user-validation'),
]
