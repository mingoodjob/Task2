from django.db import models
from user.models import UserModel

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
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title



