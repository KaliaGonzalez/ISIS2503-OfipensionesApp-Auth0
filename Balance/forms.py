from django import forms
from .models import Balance

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = [
            'precio',
            'numRegistros',
            'clasificacion',
            'mes',
            #'dateTime',
        ]

        labels = {
            'precio' : 'Precio',
            'numRegistros' : 'Numero de Registros',
            'clasificacion' : 'Clasificacion',
            'mes' : 'Mes',
            #'dateTime' : 'Date Time',
        }
