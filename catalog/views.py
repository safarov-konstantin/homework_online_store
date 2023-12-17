from django.shortcuts import render


def catalog_index(request):
    return render(request, 'catalog/index.html')


def catalog_contacts(request):
    return render(request, 'catalog/contacts.html')
