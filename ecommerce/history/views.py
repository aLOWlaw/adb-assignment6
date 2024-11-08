from rest_framework import views, generics, status
from .models import HistoryModel
from books.models import BooksModel
from books.selrializers import BooksModelSerializer
from .serializers import HistoryModelSerializer, BookSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .recommendations import get_book_recommendations
from bson import ObjectId
from rest_framework.response import Response



class HistoryCreateView(generics.CreateAPIView):
    queryset = HistoryModel.objects.all()
    serializer_class = HistoryModelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_data = serializer.validated_data.pop('book')
        book, created = BooksModel.objects.get_or_create(**book_data)
        serializer.save(user=self.request.user, book=book)


class BookRecommendationsView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user  # Assuming the user is authenticated
        print(user)
        # Fetch book recommendations
        recommendations = get_book_recommendations(user)
        
        # Serialize the recommended books
        serializer = BookSerializer(recommendations, many=True)
        
        # Return the response with recommendations
        return Response(serializer.data, status=status.HTTP_200_OK)