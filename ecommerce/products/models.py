from djongo import models

# class ImageModel(models.Model):
#     image = models.ImageField(upload_to='images/')

#     class Meta:
#         abstract = True

class ProductsModel(models.Model):
    product_id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()
    images = models.JSONField(default=list)
    stock_quantity = models.IntegerField()
    rating = models.FloatField()
    tags =  models.JSONField(default=list)

