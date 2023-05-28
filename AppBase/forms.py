from django import forms
from .models import *

GENERO_OPCIONES = [('aventura', 'Aventura'), ('deportes', 'Deportes'), ('estrategia', 'Estrategia'), ('cienciaficcion', 'Cienciaficcion'), ('hadas', 'Hadas'), ('gotica', 'Gotica'), ('policial', 'Policial'), ('guerra', 'Guerra'), ('paranormal', 'Paranormal'), ('fantastica', 'Fantastica'), ('autobiografia', 'Autobiografia'), ('detective', 'Detective'), ('educativa', 'Educativa'), ('humor', 'Humor'), ('infantil', 'Infantil'), ('juvenil', 'Juvenil'), ('thriller', 'Thriller'), ('viajes', 'Viajes'), ('ingenio', 'Ingenio'), ('agricultura', 'Agricultura'), ('botanica', 'Botanica'), ('juegos', 'Juegos'), ('recetas', 'Recetas'),]


GENERO_OPCIONES = sorted(GENERO_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class LibrosForm(forms.Form):
    nombre = forms.CharField(max_length=255)
    fecha_publicacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genero = forms.CharField(max_length=255, widget=forms.Select(choices=GENERO_OPCIONES))
    editorial = forms.CharField(max_length=255)
    descripcion = forms.CharField(max_length=255)
    valoracion = forms.IntegerField(required=True, widget=forms.Select(choices=VALORACIONES_OPCIONES))

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ('__all__')

class BuscarNombre(forms.Form):
    nombre = forms.CharField(label='Nombre del libro', max_length=255)

class BuscarGenero(forms.Form):
    genero = forms.CharField(label='Nombre del género', max_length=255, widget=forms.Select(choices=GENERO_OPCIONES))

class BuscarEditorial(forms.Form):
    editorial = forms.CharField(label='Nombre de la editorial', max_length=255)

class BuscarValoracion(forms.Form):
    valoracion = forms.IntegerField(label='Valoración', widget=forms.Select(choices=VALORACIONES_OPCIONES))

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nombre', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']

