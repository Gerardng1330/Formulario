from django import forms

from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth import get_user_model
User = get_user_model()

    
# Define un formulario basado en el modelo `Usuario`
class UserForm(forms.ModelForm):
    # Metaclase proporciona metadatos para el formulario
    class Meta:
        # Indica que el modelo asociado con este formulario es la clase `Usuario`
        model = User
        # Especifica que se deben incluir todos los campos del modelo en el formulario
        fields = '__all__'

class PasswordChangingForm(PasswordChangeForm):
    class Meta:
        # Indica que el modelo asociado con este formulario es la clase `Usuario`
        model = User
        # Especifica que se deben incluir todos los campos del modelo en el formulario
        fields = [
            'old_password',
            'new_password_1',
            'new_password_2',
        ]
        
class reset_password_form(PasswordResetForm):
    email = forms.EmailField(required=True, label='Correo', widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com'}))

""" # Enviar email para restablecer contraseña
class reset_password_form(PasswordResetForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@ejemplo.com'})) """

# cambiar la contraseña
class change_password_form(SetPasswordForm):
    new_password1 = forms.CharField(strip=True, max_length=25, required=True, label='Nueva contraseña', widget=forms.PasswordInput(attrs={'id': 'new_password_1',}))

    new_password2 = forms.CharField(strip=True, max_length=25, required=True, label='Confirmar nueva contraseña', widget=forms.PasswordInput(attrs={'id': 'new_password_2',}))