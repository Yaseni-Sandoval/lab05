from django.urls import path
from .views import update_all_products_stock

urlpatterns = [
     path('update_all_products_stock/', update_all_products_stock, name='update_all_products_stock'),
]