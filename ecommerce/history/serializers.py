from rest_framework import serializers
from .models import HistoryModel
from books.selrializers import BooksModelSerializer
from django.contrib.auth import get_user_model
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'email']


class HistoryModelSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    book = BooksModelSerializer()
    user = UserSerializer(read_only=True)

    class Meta:
        model = HistoryModel
        fields = ['_id', 'book', 'user', 'created_at', 'interaction']
