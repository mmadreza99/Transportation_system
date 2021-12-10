from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page_account, name="home_page_account"),
    path("register/", views.register, name="register"),
    path("login/", views.login_page, name="login"),
]
