from rest_framework import views, generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import ProductsModel
from .serializers import ProductsModelSerializer
from .paginations import CustomBooksPagination
from rest_framework import authentication, status, viewsets
from rest_framework.response import Response
from bson import ObjectId
from rest_framework.parsers import MultiPartParser, FormParser


class ListProductsView(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsModelSerializer
    pagination_class = CustomBooksPagination
    permission_classes = [IsAuthenticated]
    
class CreateProductsView(generics.CreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsModelSerializer
    permission_classes = [IsAdminUser] #Change
    # parser_classes = (MultiPartParser, FormParser)  # Allow file uploads

class DeleteProductsView(generics.DestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsModelSerializer
    permission_classes = [IsAdminUser] #Change
    lookup_field = '_id'

    def get_object(self):
        # Convert the string _id from URL to ObjectId
        obj_id = ObjectId(self.kwargs.get(self.lookup_field))
        return self.get_queryset().get(_id=obj_id)

class GetProductsView(generics.RetrieveAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsModelSerializer
    permission_classes = [IsAuthenticated] #Change
    lookup_field = '_id'

    def get_object(self):
        # Convert the string _id from URL to ObjectId
        obj_id = ObjectId(self.kwargs.get(self.lookup_field))
        return self.get_queryset().get(_id=obj_id)
