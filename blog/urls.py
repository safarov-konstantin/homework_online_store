from django.urls import path
from blog.apps import BlogConfig
from blog.views import PageCreateView, PageListView, PageDetailView, PageUpdateView, PageDeleteView


app_name = BlogConfig.name

urlpatterns = [
    path('create/', PageCreateView.as_view(), name='create'),
    path('', PageListView.as_view(), name='list'),
    path('view/<int:pk>/', PageDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', PageUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', PageDeleteView.as_view(), name='delete'),
]
