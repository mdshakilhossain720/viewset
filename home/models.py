from django.db import models

# Create your models here.
class Studetn(models.Model):
    name=models.CharField(max_length=100)
    dep=models.CharField(max_length=50)
    durtion=models.IntegerField()
