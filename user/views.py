from functools import partial
from venv import create
from django.contrib.auth import login, logout, authenticate
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from blog.models import Category, Article 
from user.models import UserModel, UserProfile
from user.serializers import UserSerializer,ArticleSerializer, UserProfileSerializer

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

        return Response({'message': '로그아웃 성공'})
        
class UserSignUpView(APIView):
    """
    SignUp API 요청시 사용되는 함수
    """
    # def post(self, request):
    #     password = request.POST.get('password')
    #     user = UserModel.objects.create(**request.POST.dict())
    #     user.set_password(password)
    #     user.save()
    #     return Response({'message': '회원가입 성공'})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공'})
        return Response(serializer.errors)

    def put(self, request):
        user = UserProfile.objects.get(user=request.user.id)
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
