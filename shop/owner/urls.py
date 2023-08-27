from django.urls import path
from . import views

app_name = 'owner'
urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('add_product/', views.add_product, name='add_product'),
]