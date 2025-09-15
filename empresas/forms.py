from django import forms
from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["nombre", "rfc", "direccion", "telefono", "email"]
        labels = {
            "nombre": "Nombre de la empresa",
            "rfc": "RFC",
            "direccion": "Dirección",
            "telefono": "Teléfono",
            "email": "Correo electrónico",
        }
