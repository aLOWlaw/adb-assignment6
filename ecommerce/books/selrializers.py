from rest_framework import serializers
from .models import BooksModel
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)
    

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'

class BooksModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'
        # exclude = ['_id']