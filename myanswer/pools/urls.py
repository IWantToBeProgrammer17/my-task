from django.urls import path

from . import views

urlpatterns = [
    path("kedua/", views.kedua, name="kedua"),
    path("", views.index, name="index"),
]
