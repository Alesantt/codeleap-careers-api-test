from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

def __str__(self):
    return self.title