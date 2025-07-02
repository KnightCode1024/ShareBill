from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path("hello/", views.Hello.as_view()),
]
