from rest_framework import viewsets

from categoryproduct.models import Category, Product
from categoryproduct.serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    List all categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    List all Products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
