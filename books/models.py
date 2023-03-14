from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=400, default="https://www.amazon.co.uk/")
    image = models.URLField(max_length=400, default="https://m.media-amazon.com/images/I/41gIqB7ouXL._SX326_BO1,204,203,200_.jpg")
    authors = models.JSONField(default={'name':'napoleon'})
    rating = models.CharField(max_length=10, default=5)
    ratings_total = models.CharField(max_length=10, default=10000)

    def __str__(self):
        return f"{self.id}: {self.title}"
