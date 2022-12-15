from django.urls import path
from . import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products_list, name='products_list'),
    path('<slug:slug>/', views.product_details, name='product_details'),  
]
