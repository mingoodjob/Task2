from rest_framework import serializers
from user.models import UserModel,UserProfile, Hobby
from blog.models import Category, Article, Comment
from blog.serializers import ArticleSerializer
from product.models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.thumnail = validated_data.get('thumnail', instance.thumnail)
        instance.save()
        return instance

    class Meta:
        model = ProductModel
        fields = ["author", "title", "desc", "thumnail", "created_at", "updated_at", "exposure_start", "exposure_end"]

        extra_kwargs = {
            # write_only : 해당 필드를 쓰기 전용으로 만들어 준다.
            # 쓰기 전용으로 설정 된 필드는 직렬화 된 데이터에서 보여지지 않는다.
            'title' : {
                'error_messages' : {
                    'required' : '제목을 입력해주세요.'
                },
                'required' : True
            },
            'desc' : {
                'error_messages' : {
                    'required' : '설명을 입력해주세요.'
                },
                'required' : True
            },
            'author' : {'write_only' : True},

            # 'desc': {'invalid' : '설명을 입력해주세요.', 'required' : '설명을 입력해주세요.', 'max_length' : '설명은 100자를 넘기지 말아주세요.'},
            'thumnail': {'write_only' : True,
                # error_messages : 에러 메세지를 자유롭게 설정 할 수 있다.
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    # 'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '파일 형식이 아닙니다.'
                    },
                    # required : validator에서 해당 값의 필요 여부를 판단한다.
                    'required': False # default : True
                    },
            }