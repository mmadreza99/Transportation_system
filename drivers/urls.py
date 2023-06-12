from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeDriver.as_view(), name='home_driver'),
    path('login_or_register/', views.LoginOrRegister.as_view(), name='driver_login_or_register'),
    path('register/', views.RegisterView.as_view(), name='driver_register'),
    path('login/', views.LoginView.as_view(), name='driver_login'),
    path('logout/', views.logout_view, name='driver_Logout'),
    path('register_more/',
         login_required(
             views.RegisterMoreView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_register_more'),
    path('update_more/',
         login_required(
             views.RegisterUpdateMoreView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_update_more'),
    path('register_certificate/',
         login_required(
             views.RegisterCertificateView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_register_certificate'),
    path('update_certificate/',
         login_required(
             views.RegisterUpdateCertificateView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_update_certificate'),
    path('register_truck/',
         login_required(
             views.RegisterTruckView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_register_truck'),
    path('update_truck/',
         login_required(
             views.RegisterUpdateTruckView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_update_truck'),
    path('register_kart/',
         login_required(
             views.RegisterKartView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_register_kart'),
    path('update_kart/',
         login_required(
             views.RegisterUpdateKartView.as_view(),
             login_url="/driver/login_or_register/"
         ), name='driver_update_kart'),
    path(
        'profile/',
        login_required(
            views.ProfileView.as_view(),
            login_url="/driver/login_or_register/"
        ), name='driver_profile'
    )
]
