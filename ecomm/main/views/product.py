from rest_framework import permissions
from main.models import Product, Cart
from main.serialzers.user import ProductSerializer, CartCreateSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class CartViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [permissions.AllowAny]

