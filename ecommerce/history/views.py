from rest_framework import views, generics
from .models import HistoryModel
from books.models import BooksModel
from .serializers import HistoryModelSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated



class HistoryCreateView(generics.CreateAPIView):
    queryset = HistoryModel.objects.all()
    serializer_class = HistoryModelSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        book_data = serializer.validated_data.pop('book')
        book, created = BooksModel.objects.get_or_create(**book_data)
        serializer.save(user=self.request.user, book=book)
    
