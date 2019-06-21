from django.db import models

# Create your models here.


class QuoteModel(models.Model):
    text = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
