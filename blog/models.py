from django.db import models
from pytz import timezone
from user.models import UserModel
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    exposure_start = models.DateTimeField("게시 시간", default=datetime.now)
    exposure_end = models.DateTimeField("게시 종료", default=datetime.now)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content

