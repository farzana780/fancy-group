from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product, name='product'),
    path('<slug>', views.product, name='cat_slug'),
    path('product_details/<slug>', views.product_details, name='product_details'),
]