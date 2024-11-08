from djongo import models
from books.models import BooksModel
# from authuser.models import User
from django.contrib.auth import get_user_model
from books.models import BooksModel

User = get_user_model()

INTERACTION_CHOICES = (
        ("like", "like"),
        ("purchase", "purchase"),
        ('cart', 'cart')
    )

class HistoryModel(models.Model):
    _id = models.ObjectIdField(primary_key = True)
    book = models.ForeignKey(BooksModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    interaction = models.CharField(max_length=128, choices=INTERACTION_CHOICES)