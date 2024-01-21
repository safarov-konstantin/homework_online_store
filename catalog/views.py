from django.urls import reverse_lazy
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm
from django.views.generic import (CreateView, UpdateView, DeleteView, 
                                  ListView, DetailView, TemplateView)


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContatactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')


class VersionListView(ListView):
    model = Version


class VersionDetailView(DetailView):
    model = Version


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:versions')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:versions')


class VersionDeleteView(DeleteView):
    model = Version    
    success_url = reverse_lazy('catalog:versions')
