from django.urls import path
from . import views

urlpatterns = [
    
    path('products/', views.products_list, name='products_list'),
    path('<slug:slug>/', views.product_details, name='product_details'),
    path('about/', views.about, name='about'),
    
]
