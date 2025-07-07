from django.urls import path
from api.v1.users import views

app_name = "users"

urlpatterns = [
    path("hello/", views.Hello.as_view(), name="hello"),
]
