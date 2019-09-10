from django.utils import timezone
from django.db import models
from django_resized import ResizedImageField


class Nattest(models.Model):
    photo = ResizedImageField(size=[150, 200], crop=['middle', 'center'], quality=75, upload_to='photo/')
    document = models.FileField(upload_to='document/')
    bankvoucher = models.FileField(upload_to='bankvoucher/')
    testdate = models.DateField(max_length=30)
    GRADE_CHOICES = (
        ('N5', 'N5'),
        ('N4', 'N4'),
        ('N3', 'N3'),
        ('N2', 'N2'),
        ('N1', 'N1'),
    )
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES)
    testplace = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30, )
    lastname = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(max_length=30)
    nationality = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    role = models.IntegerField(default=0, null=False)
    created = models.DateField(default=timezone.now)

    def __str__(self):
        return self.firstname
