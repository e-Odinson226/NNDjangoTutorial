from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    producer    = models.OneToOneField(User, on_delete=models.CASCADE)
    logo        = models.ImageField(default="default.jpg", width_field=600, height_field=600, upload_to="logos")
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        logo_pic = Image.open(self.logo.path)
        if logo_pic.width > 600 or logo_pic.height > 600:
            max_size = (600, 600)
            logo_pic.thumbnail(max_size)
            logo_pic.save(self.logo.path)
