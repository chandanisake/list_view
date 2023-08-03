from django.db import models

# Create your models here.
class Teacher(models.Model):
    tname=models.CharField(max_length=100)
    tage=models.IntegerField()
    tsubject=models.CharField(max_length=100)

