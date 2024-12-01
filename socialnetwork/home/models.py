from datetime import timezone

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="posts/%Y/%m/%d")
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

