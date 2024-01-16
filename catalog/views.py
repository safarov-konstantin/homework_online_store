from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView

# cbv
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContatactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html/'
