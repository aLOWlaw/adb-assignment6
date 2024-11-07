from rest_framework import serializers
from .models import HistoryModel

class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModel
        exclude = ['_id']

    def create(self, validated_data):
        product = validated_data.pop('product')
        user = self.context['request'].user._id

        history = HistoryModel.objects.create(product = product, user = user, **validated_data)
        return history
    