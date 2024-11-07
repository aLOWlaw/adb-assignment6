from django.urls import path
from .views import BooksModelCreateView, BooksModelDeleteView, BooksModelGetView, BooksModelListView


urlpatterns = [
    path('api/books/', BooksModelListView.as_view(), name='list_books'),
    path('api/books/create/', BooksModelCreateView.as_view(), name='create_book'),
    path('api/books/delete/<str:_id>/', BooksModelDeleteView.as_view(), name='delete_book'),
    path('api/books/<str:_id>/', BooksModelGetView.as_view(), name='get_book'),
]