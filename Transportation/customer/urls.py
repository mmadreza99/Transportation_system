from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_customer, name='home_customer'),
    path('login_or_register/', views.login_or_register, name='login_or_register'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
]
