from rest_framework import serializers
from user.models import UserModel,UserProfile, Hobby
from blog.models import Category, Article, Comment

class CommentSerializer(serializers.ModelSerializer):
        class Meta:
                model = Comment
                fields = ["content"]

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Article
        fields = ["title", "content", "date", "comment_set"]