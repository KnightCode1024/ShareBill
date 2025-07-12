from rest_framework import permissions


class IsEventOrganizer(permissions.BasePermission):
    message = "Вы не являетесь организаторм мероприятия"

    def has_object_permission(self, request, view, obj):
        return obj.organizer == request.user


class IsEventParticipants(permissions.BasePermission):
    message = "Вы не являетесь участником данного мероприятия"

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "event"):
            event = obj.event
        elif hasattr(obj, "group"):
            event = obj
        else:
            return False
        return request.user in event.group.participants.all()
