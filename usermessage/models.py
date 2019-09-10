from django.db import models


# Create your models here.
class Usermessage(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.name
