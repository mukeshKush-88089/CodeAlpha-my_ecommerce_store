# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),
    path('cart/', views.cart_view, name="cart"),
    
    # Naye Authentication Routes
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    
    # store/urls.py ke urlpatterns ke andar add karein
    path('process_order/', views.process_order, name="process_order"),
]