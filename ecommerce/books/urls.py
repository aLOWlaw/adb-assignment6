from django.urls import path, include
from .views import BooksModelCreateView, BooksModelDeleteView, BooksModelGetView, BooksModelListView, BooksSearchViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'booksearch', BooksSearchViewSet)

urlpatterns = [
    path('api/books/', BooksModelListView.as_view(), name='list_books'),
    path('api/books/create/', BooksModelCreateView.as_view(), name='create_book'),
    path('api/books/delete/<str:_id>/', BooksModelDeleteView.as_view(), name='delete_book'),
    path('api/books/<str:_id>/', BooksModelGetView.as_view(), name='get_book'),
    path('', include(router.urls)),
]