from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    stock       = models.BooleanField()
    date_posted = models.DateTimeField(default=timezone.now)
    producer    = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return  reverse("product:pDetail", kwargs={"id":self.id}) #f"/products/{self.id}"