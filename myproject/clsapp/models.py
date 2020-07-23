from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=35)
    author=models.CharField(max_length=35)
    price=models.FloatField(blank=False)

class Company(models.Model):
    name=models.CharField(max_length=35)
    location=models.CharField(max_length=35)
    ceo=models.CharField(max_length=35)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.id})


