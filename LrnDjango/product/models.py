from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    stock       = models.TextField(default="bruh :/")