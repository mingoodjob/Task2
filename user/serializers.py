from rest_framework import serializers
from user.models import UserModel,UserProfile, Hobby
from blog.models import Category, Article, Comment
from blog.serializers import ArticleSerializer

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ['name']

class UserProfileSerializer(serializers.ModelSerializer):
        hobby = HobbySerializer(many=True, read_only=True)
        get_hobbys = serializers.ListField(required=False)

        def update(self, instance, validated_data):
                hobby_data = validated_data.pop('get_hobbys')
                instance.hobby.set(hobby_data)
                instance.nickname = validated_data.get('nickname', instance.nickname)
                instance.address = validated_data.get('address', instance.address)
                instance.phone = validated_data.get('phone', instance.phone)
                instance.save()
                return super().update(instance, validated_data)


        class Meta:
                model = UserProfile
    
        # serializer에 사용될 model, field지정
        
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
                fields = ["user","nickname", "address", "phone", "hobby", "get_hobbys"]                


class UserSerializer(serializers.ModelSerializer):
        articles = ArticleSerializer(many=True, source='article_set', read_only=True)
        userprofile = UserProfileSerializer(read_only=True)

        def create(self, validated_data):
                password = validated_data.pop('password')
                user = UserModel(**validated_data)
                user.set_password(password)
                user.save()
                # UserProfile.objects.create(user=user, **userprofile_data)
                
                return user

        class Meta:
                # serializer에 사용될 model, field지정
                model = UserModel
                # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
                fields = ["username", "password", "fullname", "join_date", "userprofile", "articles"]


