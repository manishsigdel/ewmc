from django.db import models

# Create your models here.
from django_resized import ResizedImageField


class Schedule(models.Model):
    name = models.CharField(max_length=30)
    photo = ResizedImageField(quality=100, upload_to='schedule/')

    def __str__(self):
        return self.name
