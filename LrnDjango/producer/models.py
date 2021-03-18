from django.db import models

# Create your models here.
class Producer(models.Model):
    name    =   models.CharField(max_length=25)
    address =   models.CharField(max_length=50)
    desc    =   models.CharField(max_length=100)