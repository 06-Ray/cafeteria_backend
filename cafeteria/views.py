from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductoForm
from .models import Productos


class ProductoListView(ListView):
    model = Productos
    template_name = 'cafeteria/lista_productos.html'
    context_object_name = 'productos'
    
    def get_queryset(self):
        return Productos.objects.select_related('categoria').order_by('categoria__nombre', 'nombre')
    

class ProductoDetailView(DetailView):
    model = Productos
    template_name = 'cafeteria/detalle_producto.html'
    context_object_name = 'producto'
    
    def get_queryset(self):
        return Productos.objects.select_related('categoria')
    
    
class ProductoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'cafeteria/form_productos.html'
    success_url = reverse_lazy('inicio')
    success_message = 'El producto "%(nombre)s", a sido creado correctamente'
        
        
class ProductoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'cafeteria/form_productos.html'        
    success_url = reverse_lazy('inicio')
    success_message = 'El producto "%(nombre)s" , a sido actualizado correctamente'
           
    
class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'cafeteria/producto_eliminado.html'        
    context_object_name = 'producto'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f'El producto "{nombre}", a sido eliminado correctamente')