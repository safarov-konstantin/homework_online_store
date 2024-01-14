from importlib.resources import contents
from django.shortcuts import render
from catalog.models import Product


def catalog_index(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/index.html', context=context)


def catalog_contacts(request):
    return render(request, 'catalog/contacts.html')


def catalog_product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context=context)
