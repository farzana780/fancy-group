from django.urls import path
from . import views

app_name = 'others'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('career/', views.career, name='career'),
    path('<slug:dept_slug>', views.career,name='dept_slug'),
    path('career/details', views.job_details, name='job_details'),
    path('apply/', views.job_apply, name='job_apply'),

]
