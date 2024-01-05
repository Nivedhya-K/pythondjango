from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=250)
    author=models.CharField(max_length=200)
    year=models.IntegerField()
    desc=models.TextField()
    image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name