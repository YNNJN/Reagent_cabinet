from django.db import models
from django.contrib.auth import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFit(300, 300)],
                                     format='JPEG',
                                     options={'quality': 60})

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)