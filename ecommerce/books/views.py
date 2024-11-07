
from .models import BooksModel
from .selrializers import BooksModelSerializer, BooksModelCreateSerializer
from .paginations import CustomBooksPagination
from rest_framework import generics
from rest_framework.permissions import AllowAny
from bson import ObjectId

class BooksModelListView(generics.ListAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    pagination_class = CustomBooksPagination
    permission_classes = [AllowAny]

class BooksModelCreateView(generics.CreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelCreateSerializer
    permission_classes = [AllowAny]

class BooksModelDeleteView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    permission_classes = [AllowAny]
    lookup_field = '_id'

    def get_object(self):
        # Convert the string _id from URL to ObjectId
        obj_id = ObjectId(self.kwargs.get(self.lookup_field))
        return self.get_queryset().get(_id=obj_id)    

class BooksModelGetView(generics.DestroyAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BooksModelSerializer
    permission_classes = [AllowAny]
    lookup_field = '_id'

    def get_object(self):
        # Convert the string _id from URL to ObjectId
        obj_id = ObjectId(self.kwargs.get(self.lookup_field))
        return self.get_queryset().get(_id=obj_id)    
