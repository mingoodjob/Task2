from rest_framework import serializers
from user.models import UserModel,UserProfile, Hobby
from blog.models import Category, Article, Comment
from blog.serializers import ArticleSerializer

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['name']

class UserProfileSerializer(serializers.ModelSerializer):
        hobby = HobbySerializer(many=True)
        class Meta:
                model = UserProfile
    
        # serializer에 사용될 model, field지정
        
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
                fields = ["nickname", "address", "phone", "hobby"]                


class UserSerializer(serializers.ModelSerializer):
        article_set = ArticleSerializer(many=True)
        # comment = CommentSerializer()
        userprofile = UserProfileSerializer()
        # user = serializers.SerializerMethodField()

        class Meta:
                # serializer에 사용될 model, field지정
                model = UserModel
                # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
                fields = ["username", "fullname", "join_date", "userprofile","article_set"]


