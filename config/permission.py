from urllib import response
from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code = status_code
        super().__init__(detail=detail, code=code)

class RegistedMoreThanAWeekUser(BasePermission):
    """
    가입일 기준 1주일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 1주일 이상 지난 사용자만 사용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=1)))

# admin write permission
class AdminWritePermission(BasePermission):
    """
    관리자 및 가입일 기준 1주일 이상 지난 사용자만 접근 가능
    """
    SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

    message = '관리자 혹은 가입일이 7일이상인 유저만 접근 가능 합니다.'
        
    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                'message': '로그인이 필요합니다.'
            }    
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        elif user.is_authenticated and request.method in self.SAFE_METHODS:
            print(user.username)
            print(self.SAFE_METHODS)
            return True
        
        elif user.is_authenticated and user.join_date < (timezone.now() - timedelta(minutes=60*24*7)):
            print(user.join_date)
            print(timezone.now() - timedelta(minutes=60*24*7))
            return True
        
        elif user.is_authenticated and user.is_admin:
            return True


        # return bool(request.user and request.user.is_admin or request.user.join_date < (timezone.now() - timedelta(minutes=60*24*7)))