from django.contrib import admin
from .models import Categoria, Productos

class ProductoInline(admin.TabularInline):
    model = Productos
    extra = 3
    fields = ['sku', 'nombre', 'estado','precio', 'stock_disponible', 'fecha_ingreso']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion']
    search_fields = ['nombre']
    inlines = [ProductoInline]
    
    
@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['sku', 'nombre', 'descripcion', 'estado']
    list_filter = ['estado', 'categoria']
    search_fields = ['nombre', 'sku']
