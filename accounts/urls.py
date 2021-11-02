from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views.student import register_view, login_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]