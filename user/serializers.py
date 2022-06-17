from rest_framework import serializers
from user.models import UserModel,UserProfile
from blog.models import Category, Article, Comment

class UserProfileSerializer(serializers.ModelSerializer):

        class Meta:
                model = UserProfile
    
        # serializer에 사용될 model, field지정
        
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
                fields = ["nickname", "address", "phone", "hobby"]

class CommentSerializer(serializers.ModelSerializer):
        class Meta:
                model = Comment
                fields = ["content"]
                

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Article
        fields = ["title", "content", "date", "comment_set"]

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


