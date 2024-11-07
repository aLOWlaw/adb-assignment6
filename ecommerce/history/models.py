from djongo import models
from products.models import ProductsModel
from authuser.models import User

ITERACTION_CHOICES = (
        ("like", "like"),
        ("purchase", "purchase")
    )

class HistoryModel(models.Model):
    _id = models.ObjectIdField(primary_key = True)
    product = models.EmbeddedField(model_container=ProductsModel)
    user = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    iteraction = models.CharField(max_length=128, choices=ITERACTION_CHOICES)