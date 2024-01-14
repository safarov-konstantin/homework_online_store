from django.urls import path
from catalog.views import catalog_index, catalog_contacts, catalog_product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', catalog_index, name='index'),
    path('contacts/', catalog_contacts, name='contacts'),
    path('<int:pk>/product/', catalog_product, name='product'),
]
