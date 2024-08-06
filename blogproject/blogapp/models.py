from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from  django.utils import timezone
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255 )
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.author} | {self.title}'
    def get_absolute_url(self):
        return reverse('home')

