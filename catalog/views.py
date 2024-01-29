from django.urls import reverse_lazy
from django.forms import inlineformset_factory
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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)    
        else:
            context_data['formset'] = VersionFormset(instance=self.object) 
        return context_data
    
    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        if formset.is_valid():
           formset.instance = self.object
           formset.save() 
        return super().form_valid(form)     


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)    
        else:
            context_data['formset'] = VersionFormset(instance=self.object) 
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
           formset.instance = self.object
           formset.save() 
        return super().form_valid(form)       


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
