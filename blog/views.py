from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from blog.models import Category, Article, Comment
from user.models import UserModel
from config.permission import RegistedMoreThanAWeekUser
from config.permission import AdminWritePermission
from user.serializers import ArticleSerializer
from datetime import datetime

# Create your views here.
class UserPostView(APIView):
    permission_classes = [AdminWritePermission]
    """

    """
    def get(self, request):
        articles = Article.objects.filter(exposure_start__lte=datetime.now(), exposure_end__gte=datetime.now()).order_by('-date')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        category = request.data.get('category', [])
        exposure_start = request.data.get('exposure_start')
        exposure_end = request.data.get('exposure_end')

        author = UserModel.objects.get(username=request.user)

        if len(title) < 5:
            return Response({'message': '제목은 5자 이상이어야 합니다.'})
        if len(content) < 20:
            return Response({'message': '내용은 20자 이상이어야 합니다.'})
        if category == []:
            return Response({'message': '카테고리를 선택해주세요.'})

        article = Article(title=title, content=content, author=request.user, exposure_start=exposure_start, exposure_end=exposure_end)
        category = request.data.pop('category')
        article.save()
        article.category.add(*category)
        
        return Response({'message': '게시글이 작성되었습니다.'})

    def put(self, request):
        author = UserModel.objects.get(username=request.user) 
        article = Article.objects.get(id=request.data.get('id'))
        content = request.data.get('content')

        if len(content) < 10:
            return Response({'message': '내용은 10자 이상이어야 합니다.'})

        Comment.objects.create(article=article, content=content, author=author)

        return Response({'message': '댓글이 작성되었습니다.'})    
