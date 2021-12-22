from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("home", views.home_page_blog, name="home_page_blog"),
    path("register/", views.register, name="register"),
    path("login/", views.login_page, name="login"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
