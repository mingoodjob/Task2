from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from blog.models import Category, Article, Comment
from user.models import UserModel
from config.permission import RegistedMoreThanAWeekUser
from user.serializers import ArticleSerializer

# Create your views here.
class UserPostView(APIView):
    permission_classes = [RegistedMoreThanAWeekUser]
    """

    """
    def get(self, request):
        article_data = ArticleSerializer(Article.objects.filter(author=request.user), many=True).data
        return Response(article_data)

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        category = request.data.get('category')
        
        author = UserModel.objects.get(username=request.user)

        if len(title) < 5:
            return Response({'message': '제목은 5자 이상이어야 합니다.'})
        elif len(content) < 20:
            return Response({'message': '내용은 20자 이상이어야 합니다.'})
        elif category == '' or None:
            return Response({'message': '카테고리를 선택해주세요.'})

        category = Category.objects.get(name=request.data.get('category'))
        article = Article(title=title, content=content, author=author)
        article.save()
        article.category.add(category)

        return Response({'message': '게시글이 작성되었습니다.'})

    def put(self, request):
        author = UserModel.objects.get(username=request.user) 
        article = Article.objects.get(id=request.data.get('id'))
        content = request.data.get('content')

        if len(content) < 10:
            return Response({'message': '내용은 10자 이상이어야 합니다.'})

        Comment.objects.create(article=article, content=content, author=author)

        return Response({'message': '댓글이 작성되었습니다.'})    
