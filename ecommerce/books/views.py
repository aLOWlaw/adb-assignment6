
from .models import BooksModel
from .selrializers import BooksModelSerializer, BooksModelCreateSerializer
from .paginations import CustomBooksPagination
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from bson import ObjectId
from rest_framework.decorators import action
from rest_framework.response import Response
from pymongo import MongoClient


class BooksModelListView(generics.ListAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    pagination_class = CustomBooksPagination
    permission_classes = [IsAuthenticated]

class BooksModelCreateView(generics.CreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelCreateSerializer
    permission_classes = [IsAdminUser]

class BooksModelDeleteView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    permission_classes = [IsAdminUser]
    lookup_field = '_id'

    def get_object(self):
        # Convert the string _id from URL to ObjectId
        obj_id = ObjectId(self.kwargs.get(self.lookup_field))
        return self.get_queryset().get(_id=obj_id)    

class BooksModelGetView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = '_id'

    def get_object(self):
        # Convert the string _id from URL to ObjectId
        obj_id = ObjectId(self.kwargs.get(self.lookup_field))
        return self.get_queryset().get(_id=obj_id)    

class BooksSearchViewSet(viewsets.ModelViewSet):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def search(self, request):
        title = request.GET.get('title', None)
        description = request.GET.get('description', None)
        category = request.GET.get('category', None)
        author = request.GET.get('author', None)
        publisher = request.GET.get('publisher', None)

        # client = MongoClient("localhost", 27017)
        # db = client.assignment6
        # collection = db.books_booksmodel

        # search_terms = ' '.join(filter(None, [title, description, category, author, publisher]))
        # query = {'$text': {'$search': search_terms}} if search_terms else {}

        # items = collection.find(query)

        # Build MongoDB text search query using the $text operator
        query = {}
        if title:
            query["title"] = title
        if description:
            query["description"] = description
        if category:
            query["category"] = category
        if author:
            query["author"] = author
        if publisher:
            query["pupblisher"] = publisher

        items_list = BooksModel.objects.filter(**query)
        # Return the filtered results
        serializer = self.get_serializer(items_list, many=True)
        return Response(serializer.data)