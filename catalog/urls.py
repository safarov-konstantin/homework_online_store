from django.urls import path
from catalog.views import catalog_index


urlpatterns = [
    path('', catalog_index)
]
