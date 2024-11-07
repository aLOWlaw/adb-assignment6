from rest_framework import serializers
from .models import ProductsModel

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImageModel
#         fields = ['image']

class ProductsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = '__all__'

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = ProductsModel.objects.create(**validated_data)
        for image in images_data:
            product.images.append(image)
        product.save()
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', []) 
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.tags = validated_data.get('tags', instance.tags)
        
        instance.save()

        instance.images.clear()  # Clear previous images
        for image in images_data:
            instance.images.append(image)
        instance.save()

        return instance

    

        
    