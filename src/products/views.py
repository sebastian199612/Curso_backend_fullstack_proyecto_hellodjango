from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic  import (
    ListView,
    DetailView,
    RedirectView,
    CreateView,
    UpdateView,  
    DeleteView,
    )
from django.shortcuts import render , get_object_or_404

from .forms import ProductModelForm

from .mixins import TemplateTitleMixin 
from .models import Product , DigitalProduct



# Vista de creación 
class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm
    template_name = "forms.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProductModelForm 
    template_name = "products/product_detail.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return self.object.get_edit_url() 

class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "forms-delete.html"

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def get_success_url(self):
        return "/products/products"



class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        pk = kwargs.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.slug
        return f"/products/products/{slug}"

class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = kwargs.get("slug")
        return f"/products/products/{slug}"

class ProductListView(TemplateTitleMixin, ListView):
    model = Product
    title = "Productos fisicos"
    template_name = "products/product_list.html"

class ProductDetailView(DetailView):
    model = Product

class DigitalProduct(TemplateTitleMixin, ListView):
    model = DigitalProduct
    template_name = "products/product_list.html"
    title = "Productos digitales"

class ProtectedProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/product_detail.html"
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)


#vista de listado  protegida para usuarios

class ProtectedListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/product_list.html"
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
