from django.urls import path
# from catalog.views import catalog_index, catalog_contacts, catalog_product
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView, 
    ProductDetailView, 
    ContatactTemplateView, 
    ProductCreateView, 
    ProductUpdateView, 
    VersionListView, 
    VersionCreateView, 
    VersionUpdateView, 
    VersionDetailView,
    VersionDeleteView
)


app_name = CatalogConfig.name


urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contacts/', ContatactTemplateView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('create_product/', ProductCreateView.as_view(), name='create_product'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='edit_product'),
    path('versions/', VersionListView.as_view(), name='versions'),
    path('<int:pk>/version/', VersionDetailView.as_view(), name='version'),
    path('create_version/', VersionCreateView.as_view(), name='create_version'),
    path('<int:pk>/edit_version/', VersionUpdateView.as_view(), name='edit_version'),
    path('<int:pk>/delete_version/', VersionDeleteView.as_view(), name='delete_version'),
]
