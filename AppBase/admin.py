from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Libro)
admin.site.register(Resena)
admin.site.register(Avatar)
admin.site.register(Tema)
admin.site.register(Comentario)