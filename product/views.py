from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import ProductModel, ReviewModel
from product.serializers import ProductSerializer, ReviewSerializer
from user.models import UserModel
from rest_framework import status
from config.permission import AdminWritePermission
from django.db.models.query_utils import Q
from datetime import datetime

# Create your views here.
class ProductView(APIView):
    permission_classes = [AdminWritePermission]

    def get(self, request):
        products = Q(exposure_start__lte=datetime.now()) & Q(exposure_end__gte=datetime.now()) & Q(author=request.user) & Q(active=True)
        products = ProductModel.objects.filter(products)
        serializer = ProductSerializer(products, many=True).data
        return Response(serializer)

    def post(self, request):
        author = UserModel.objects.get(id=request.user.id)
        request.data['author'] = author.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        product = ProductModel.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewView(APIView):
    permission_classes = [AdminWritePermission]

    def get(self, request, id):
        reviews = ReviewModel.objects.filter(product_id=id)
        serializer = ReviewSerializer(reviews, many=True).data
        return Response(serializer)