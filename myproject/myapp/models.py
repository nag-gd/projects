from django.db import models


class Friends(models.Model):
    name = models.CharField(max_length=32)
    profession = models.CharField(max_length=64)
    organization = models.CharField(max_length=64)
    working_city = models.CharField(max_length=32)
    phone = models.IntegerField()