from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from main.models import Product
from main.serialzers.user import ProductSerializer
from main.serialzers import UserSerializer
from rest_framework import viewsets


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer