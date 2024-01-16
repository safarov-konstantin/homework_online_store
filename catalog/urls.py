from django.urls import path
# from catalog.views import catalog_index, catalog_contacts, catalog_product
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContatactTemplateView


app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContatactTemplateView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
]
