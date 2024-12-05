from rest_framework import serializers
from django.contrib.auth import get_user_model

from main.models import Cart, Product, CartItem

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", )

    
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"


class CartItemModelSerialzer(serializers.Serializer):

    class Meta:
        model = CartItem
        fields = "__all__"


class NewCartCartItemSerializer(serializers.Serializer):

    class Meta:
        model = CartItem
        fields = ("product", "count")
    

class CartCreateSerializer(serializers.ModelSerializer):

    cart_item = NewCartCartItemSerializer()

    def create(self, validated_data):
        user = self.context["user"]
        cart = Cart.objects.create(
            user=user
        )
        cartItemData = {
            **validated_data.pop("cart_item"), 
            cart : cart.id
        }
        serialzer = CartItemModelSerialzer(data=cartItemData)
        serialzer.is_valid()
        serialzer.save()
        
        return {
            "id" : cart.id
        }


    class Meta:
        model = Cart
        field = "__all__"
