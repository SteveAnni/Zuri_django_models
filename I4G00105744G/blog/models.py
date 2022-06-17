from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Test = models.TextField(max_length=23)
    Author= models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Created_date=models.DateTimeField()
    Published_date=models.DateTimeField()
    




