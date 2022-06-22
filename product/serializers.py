from rest_framework import serializers
from product.models import ProductModel, ReviewModel
from datetime import datetime, timezone
from dateutil.tz import gettz
from django.db.models import Avg

TODAY = datetime.now(gettz('Asia/Seoul'))

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ["id", "product", "content", "rating"]

class ProductSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # custom validation pattern
        if data.get('exposure_end') < TODAY:
            raise serializers.ValidationError(
                detail={"error": "종료 일자가 현재 일자보다 이전입니다."},
                )

        return data  

    def create(self, validated_data):
        validated_data['desc'] = validated_data['desc'] + f'\n생성시간 {TODAY} 생성된 상품입니다.'
        return ProductModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data['desc'] = validated_data['desc'] + f'\n업데이트시간 {TODAY} 업데이트된 상품입니다.'
        for key, value in validated_data.items():
            # if key == "desc":
            #     continue
            setattr(instance, key, value)
        instance.save()
        return instance

    # review = ReviewSerializer(many=True, source='reviewmodel_set', read_only=True)
    reviews = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()

    def get_rating_avg(self, obj):
        return obj.reviewmodel_set.all().aggregate(avg=Avg('rating'))['avg']

    def get_reviews(self, obj):
        reviews_data = []
        for review in obj.reviewmodel_set.all():
            review_data = {
                "product_id" : review.product.id,
                "product_title" : review.product.title,
                "review_content" : review.content,
                "review_rating" : review.rating,
            }
            reviews_data.append(review_data)
        return reviews_data
        
    class Meta:
        
        model = ProductModel
        fields = ["author", "title", "desc", "price", "thumnail", "created_at", "updated_at", "rating_avg", "exposure_start", "exposure_end", "reviews"]

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