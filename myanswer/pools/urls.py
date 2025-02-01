from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("kedua/", views.kedua, name="kedua"),
]