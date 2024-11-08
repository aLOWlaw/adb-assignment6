from djongo import models


class BooksModel(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=128)
    publisher = models.CharField(max_length=128)
    
    # class Meta:
    #     indexes = [
    #         models.Index(fields=['title']),
    #         models.Index(fields=['author']),
    #         models.Index(fields=['category']),
    #         models.Index(fields=['description']),
    #         models.Index(fields=['publisher']),
    #     ]
