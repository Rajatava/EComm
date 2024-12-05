from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Create your models here.


class Product(models.Model):

    name = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    

    class CATEGORY_CHOICES(models.TextChoices):
        FOOD = "1", "FOOD"
        CLOTH = "2", "CLOTH"

    category = models.CharField(max_length=125,
        choices=CATEGORY_CHOICES.choices
    )


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    class STATUS_CHOICES(models.TextChoices):
        PENDING = "1", "PENDING"
        COMPLETED = "2", "COMPLETED"

    status = models.CharField(max_length=125,
        choices=STATUS_CHOICES.choices,
        default=STATUS_CHOICES.PENDING
    )
    create_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)




    
