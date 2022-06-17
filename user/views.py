from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from blog.models import Category, Article 
from user.models import UserModel
from user.serializers import UserSerializer,ArticleSerializer


class UserApiView(APIView):
    """
    Login API 요청시 사용되는 함수
    사용자가 입력한 아이디와 비밀번호를 받아서
    인증된 사용자를 반환하는 함수
    인증된 사용자가 없을 경우 None을 반환함
    인증된 사용자가 있을 경우 인증된 사용자를 반환함
    """
    
    def get(self, request):
        user = request.user
        userd = UserModel.objects.get(username=user)
        article = Article.objects.filter(author=userd)
        print(dir(article))
        user_data = UserSerializer(user).data
        return Response(user_data)
 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': '로그인 성공'})
        return Response({'message': '로그인 실패'})
    
    def delete(self, request):
        #로그아웃
        logout(request)
        


    