from django import forms
from .models import Carrera

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = '__all__'
        labels = {
            'nombre': 'Nombre de la carrera',
            'siglas': 'Siglas de la carrera',
            'facultad': 'Facultad a la que pertenece'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de la carrera'
                }
            ),
            'siglas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese las siglas de la carrera'
                }
            ),
            'facultad': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }