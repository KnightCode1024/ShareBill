from django.urls import include, path

urlpatterns = [
    path("users/", include("api.v1.users.urls")),
    path("events/", include("api.v1.events.urls")),
    path("receipts/", include("api.v1.receipts.urls")),
]
