from django.urls import include, path

from main.views import ProductViewSet, CreateUserView, CartViewSet

urlpatterns = [
    path('user/', CreateUserView.as_view()),
    path('product/', ProductViewSet.as_view({'get' : 'list', 'post' : 'create' })),
    path('product/<int:pk>/', ProductViewSet.as_view({'get' : 'retrieve', 'patch' : 'partial_update', 'delete' : 'destroy'})),
    path('cart/', CartViewSet.as_view({'post' : 'create'}))
]