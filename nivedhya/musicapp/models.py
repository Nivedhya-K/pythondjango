from django.db import models

# Create your models here.
class Cakes(models.Model):
    name=models.CharField(max_length=150)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
def __str__(self):
             return self.name
class Place(models.Model):
     name1=models.CharField(max_length=200)
     image1=models.ImageField(upload_to='pics')
     desc1=models.TextField()
def __str__(self):
            return self.name1