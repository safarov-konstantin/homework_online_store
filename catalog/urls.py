from django.urls import path
# from catalog.views import catalog_index, catalog_contacts, catalog_product
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, catalog_contacts


app_name = CatalogConfig.name

# urls cbv
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', catalog_contacts, name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
]

# urls fbv
# urlpatterns = [
#     path('', catalog_index, name='index'),
#     path('contacts/', catalog_contacts, name='contacts'),
#     path('<int:pk>/product/', catalog_product, name='product'),
# ]
