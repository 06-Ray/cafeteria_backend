from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Productos

def lista_productos(request):
    productos =  Productos.objects.all().select_related('categoria')
    categorias = Categoria.objects.all()
    
    contexto = {
        'productos': productos,
        'categorias': categorias,
    }
    
    return render(request, 'base.html', contexto)