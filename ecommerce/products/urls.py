from django.urls import path
from .views import ListProductsView, CreateProductsView, DeleteProductsView, GetProductsView


urlpatterns = [
    path('api/products/', ListProductsView.as_view(), name='list_books'),
    path('api/products/create/', CreateProductsView.as_view(), name='create_book'),
    path('api/products/delete/<str:_id>/', DeleteProductsView.as_view(), name='delete_book'),
    path('api/products/<str:_id>/', GetProductsView.as_view(), name='get_book'),
]
