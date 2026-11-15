from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre de la categoría')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    
    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre del producto')
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripción')
    estado = models.BooleanField(default=True,  verbose_name='Disponible')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio ($ CLP)')
    stock_disponible = models.IntegerField(verbose_name='Producto disponible')
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', verbose_name='Categoría')
    
    def __str__(self):
        return f'{self.nombre} - {self.descripcion}'