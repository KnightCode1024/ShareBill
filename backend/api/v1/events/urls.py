from django.urls import path
from api.v1.events import views

app_name = "events"

urlpatterns = [
    path(
        "",
        views.AddEventView.as_view(),
        name="add",
    ),
    path(
        "<int:pk>/",
        views.EventView.as_view(),
        name="event",
    ),
    path(
        "group/join/<uuid:invite_token>/",
        views.JoinGroupView.as_view(),
        name="join",
    ),
    path(
        "select/receipt/item/<int:pk>/",
        views.SelectItemView.as_view(),
        name="select_item",
    ),
    path(
        "receipts/<int:pk>/",
        views.ReceiptsPositions.as_view(),
        name="receipts",
    ),
]
