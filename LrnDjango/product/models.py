from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    stock       = models.BooleanField()

    def get_absolute_url(self):
        return  reverse("product:pDetail", kwargs={"id":self.id}) #f"/products/{self.id}"