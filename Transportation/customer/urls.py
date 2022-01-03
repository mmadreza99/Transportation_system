from django.contrib.auth.decorators import login_required

from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeCustomer.as_view(), name='home_customer'),
    path('login_or_register/', views.LoginOrRegister.as_view(), name='customer_login_or_register'),
    path('register/', views.RegisterView.as_view(), name='customer_register'),
    path('login/', views.LoginView.as_view(), name='customer_login'),
    path('logout/', views.logout_view, name='customer_Logout'),
    path('profile/',
         login_required(
             views.ProfileView.as_view(),
             login_url="/customer/login_or_register/"
         ), name='customer_profile'),
    path('customer_more/',
         login_required(
             views.CreateCustomerMore.as_view(),
             login_url="/customer/login_or_register/"
         ), name='customer_more'),
    path('consignment/',
         login_required(
             views.ConsignmentListView.as_view(),
             login_url="/customer/login_or_register/"
         ), name='customer_consignment'),
    path('consignment/<int:pk>/',
         login_required(
             views.ConsignmentDetailView.as_view(),
             login_url="/customer/login_or_register/"
         ), name='detail_consignment'),
    path('consignment/create_consignment/',
         login_required(
             views.CreateConsignmentView.as_view(),
             login_url="/customer/login_or_register/"
         ), name='create_consignment'),
    path('consignment/update_consignment/<int:pk>/',
         login_required(
             views.UpdateConsignmentView.as_view(),
             login_url="/customer/login_or_register/"
         ), name='update_consignment'),
]
