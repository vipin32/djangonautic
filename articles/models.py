from django.db import models

# Create your models here.
class Article(models.Models):
    title = models.charField(max_length=100)
    slug = models.slugField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
