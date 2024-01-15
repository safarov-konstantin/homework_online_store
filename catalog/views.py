from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView, DetailView

# cbv
class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# fbv 
def catalog_contacts(request):
    return render(request, 'catalog/contacts.html')


# def catalog_index(request):
#     context = {
#         'object_list': Product.objects.all()
#     }
#     return render(request, 'catalog/index.html', context=context)


def catalog_product(request, pk):
    context = {
        'object': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context=context)
