from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name
