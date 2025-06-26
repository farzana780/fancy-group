from django.contrib import admin
from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('search/', views.search, name='search'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('term_conditions/', views.term_conditions, name='term_conditions'),

]
