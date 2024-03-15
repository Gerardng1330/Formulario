from django import forms
from .models import User
from django.contrib.auth.forms import PasswordChangeForm

    
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
            'new_password1',
            'new_password2',
        ]