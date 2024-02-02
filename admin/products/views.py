# from urllib import response

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from admin.products.producer import publish

from products.models import Product, User

from products.serializers import ProductSerlizers
import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Product.objects.all()
        serilizer =  ProductSerlizers(products, many=True)
        publish()
        return Response(serilizer.data)
        
    def create(self): # /api/products
        serializer = ProductSerlizers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serilizer = ProductSerlizers(product)
        return Response(serilizer.data)
    
    def update(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serilizer = ProductSerlizers(isinstance=product, data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data, status=status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
    
    
        