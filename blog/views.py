from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from blog.models import Category, Article 
from user.models import UserModel

# Create your views here.
class UserPostView(APIView):
    """

    """
    def get(self, request):
        posts = []
        username = UserModel.objects.get(username=request.user)
        articles = Article.objects.filter(author=username)
        for article in articles:
            titles = {
                'author': article.author.username,
                'title': article.title,
                'content': article.content,
                'date': article.date
            }
            posts.append(titles)
        return Response({'post': posts})