from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=140) 
    body=models.TextField(max_length=500)
    date=models.DateTimeField("Published")

    def __str__(self):
        return self.title