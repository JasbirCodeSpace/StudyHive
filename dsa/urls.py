from django.urls import path
from dsa.views import dsa

urlpatterns = [
    path("", dsa.index, name="dsa")
]
