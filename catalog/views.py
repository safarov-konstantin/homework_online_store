from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm
from django.views.generic import (CreateView, UpdateView, DeleteView, 
                                  ListView, DetailView, TemplateView)
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContatactTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
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


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        _user = self.request.user
        _instance = self.get_object()
        
        custom_perms = (
            'catalog.set_is_published',
            'catalog.set_category',
            'catalog.set_description',
        )
    
        if _user == _instance.author:
            return True
        elif _user.groups.filter(name='moderator') and _user.has_perms(custom_perms):
            return True
        return self.handle_no_permission()


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
