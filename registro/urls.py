from django.urls import path
from . import views

urlpatterns = [
    #path('registro1/', views.registros, name='registro1'),
    path('success/', views.success, name='success'),
    path('send-token/', views.send_token, name='send-token'),
    path('verify/<auth_token>' , views.verify ,name = "verify"),
    path('error/' , views.error_page , name = "error")
]
