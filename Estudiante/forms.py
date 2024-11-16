from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre', 
            'edad',
            'curso',
            'matricula',
        ]
        labels = {
            'nombre': 'Nombre', 
            'edad': 'Edad',
            'curso': 'Curso',
            'matricula': 'Matricula',
        }