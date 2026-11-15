from django.contrib import admin
from .models import Categoria, Productos

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']
    
    
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['sku', 'nombre', 'descripcion', 'estado']
    list_filter = ['estado', 'categoria']
    search_fields = ['nombre', 'sku']
