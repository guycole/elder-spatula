from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page3", views.page3, name="page3"),
]