from django.urls import path
from catalog.views import catalog_index, catalog_contacts


urlpatterns = [
    path('', catalog_index),
    path('contacts/', catalog_contacts)
]
