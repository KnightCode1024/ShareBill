from django.urls import path
from api.v1.events import views

app_name = "events"

urlpatterns = [
    path("", views.AddEventView.as_view(), name="add"),
    path("<int:pk>/", views.EventView.as_view()),
    path("group/join/<uuid:invite_token>", views.JoinGroupView.as_view()),
]
