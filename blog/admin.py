from django.contrib import admin

# Register your models here.
from .models import Articulo, Categoria

admin.site.register(Articulo)
admin.site.register(Categoria)