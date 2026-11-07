
from django import forms
from .models import marca, moto, resena


# FORMULARIO DE MARCAS
class MarcaForm(forms.ModelForm):

    class Meta:
        model = marca
        fields = [
            'nombre',
            'pais_origen'
        ]


# FORMULARIO DE MOTOS
class MotoForm(forms.ModelForm):

    class Meta:
        model = moto
        fields = [
            'nombre',
            'marca',
            'cilindraje',
            'potencia',
            'velocidad_maxima',
            'precio'
        ]


# FORMULARIO DE RESEÑAS
class ResenaForm(forms.ModelForm):

    class Meta:
        model = resena
        fields = [
            'moto',
            'autor',
            'comentario'
        ]
