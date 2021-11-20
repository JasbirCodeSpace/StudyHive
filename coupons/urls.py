from django.conf.urls import url
from django.urls import path
from coupons.views import show_coupons
urlpatterns = [
    path("", show_coupons, name="show-coupons"),
]
