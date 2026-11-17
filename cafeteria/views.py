from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductoForm
from .models import Productos, Categoria


class ProductoListView(ListView):
    model = Productos
    template_name = 'lista_productos.html'
    context_object_name = 'productos'
    
    def get_categoria_activa(self):
        categoria = self.request.GET.get('categoria')
        return int(categoria) if categoria and categoria.isdigit() else None
    
    def get_queryset(self):
        productos = Productos.objects.select_related('categoria').order_by('categoria__nombre', 'nombre')
        categoria = self.get_categoria_activa()
        if categoria:
            productos = productos.filter(categoria_id=categoria)
        return productos
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['categorias'] = Categoria.objects.all()
        contexto['categoria_activa'] = self.get_categoria_activa()
        return contexto

class ProductoDetailView(DetailView):
    model = Productos
    template_name = 'detalle_producto.html'
    context_object_name = 'producto'
    
    def get_queryset(self):
        return Productos.objects.select_related('categoria')
    
    
class ProductoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'form_productos.html'
    success_url = reverse_lazy('inicio')
    success_message = 'El producto "%(nombre)s", a sido creado correctamente'
        
        
class ProductoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = 'form_productos.html'        
    success_url = reverse_lazy('inicio')
    success_message = 'El producto "%(nombre)s" , a sido actualizado correctamente'
           
    
class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Productos
    template_name = 'producto_eliminado.html'        
    context_object_name = 'producto'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        nombre = self.object.nombre
        response = super().form_valid(form)
        messages.success(self.request, f'El producto "{nombre}", a sido eliminado correctamente')
        return response