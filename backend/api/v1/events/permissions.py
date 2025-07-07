from rest_framework import permissions


class IsEventOrganizer(permissions.BasePermission):
    message = "Вы не являетесь организаторм мероприятия"

    def has_object_permission(self, request, view, obj):
        return obj.organizer == request.user
