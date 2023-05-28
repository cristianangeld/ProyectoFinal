from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-libro', agregar_libro, name="AgregarLibro"),
    path('l-libros', lista_libros, name="ListaLibros"),
    path('el-libros/<int:id>', eliminar_libro, name="EliminarLibro"),
    path('ed-libros/<int:id>', editar_libro, name="EditarLibro"),
    path('ag-resena', agregar_resena, name='AgregarResena'),
    path('l-resenas', lista_resenas, name='ListaResenas'),
    path('el-resenas/<int:id>', eliminar_resena, name="EliminarResena"),
    path('ed-resenas/<int:id>', editar_resena, name="EditarResena"),
    path('busq-libro', busqueda_libros, name="BusquedaLibros"),
    path('buscar-nombre', buscar_nombre, name="BuscarNombre"),
    path('buscar-genero', buscar_genero, name="BuscarGenero"),
    path('buscar-editorial', buscar_editorial, name="BuscarEditorial"),
    path('buscar-valoracion', buscar_valoracion, name="BuscarValoracion"),
    path('about-me', AboutMe, name="AboutMe"),
    path('foro', lista_temas, name='Foro'),
    path('crear-tema', crear_tema, name='CrearTema'),
    path('ed-tema/<int:pk>', editar_tema, name='EditarTema'),
    path('el-tema/<int:pk>', eliminar_tema, name='EliminarTema'),
    path('foro/<int:pk>/', detalle_tema, name='DetalleTema'),
    path('<int:pk>/crear-coment', crear_comentario, name='CrearComentario'),
]
