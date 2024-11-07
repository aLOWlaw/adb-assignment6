from rest_framework import serializers
from .models import BooksModel

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'

class BooksModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'
        # exclude = ['_id']