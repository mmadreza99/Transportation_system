from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path("login-or-register", views.home_page_blog, name="blog_login_or_register"),
    path("register/", views.register, name="blog-register"),
    path("login/", views.login_page, name="blog-login"),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
