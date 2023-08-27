from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/purchase/', views.purchase_product, name='purchase_product'),
]