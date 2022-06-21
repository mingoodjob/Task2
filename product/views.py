from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import ProductModel
from product.serializers import ProductSerializer
from user.models import UserModel
from rest_framework import status
from datetime import datetime

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        products = ProductModel.objects.filter(exposure_start__lte=datetime.now(), exposure_end__gte=datetime.now()).filter(author=request.user.id)
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