# forms.py

from django import forms
from .models import Usuario


# Define un formulario basado en el modelo `Usuario`
class UsuarioForm(forms.ModelForm):
    # Metaclase proporciona metadatos para el formulario
    class Meta:
        # Indica que el modelo asociado con este formulario es la clase `Usuario`
        model = Usuario
        # Especifica que se deben incluir todos los campos del modelo en el formulario
        fields = '__all__'
