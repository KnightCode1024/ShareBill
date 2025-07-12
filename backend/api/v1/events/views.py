from rest_framework import status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response


from api.v1.events.serializers import (
    AddEventSerializer,
    EventSerializer,
    JoinGroupResponseSerializer,
    ReceiptSerializer,
    ReceiptItemSerializer,
    SelectItemSerializer,
    ReceiptNameItemSerializer,
)
from api.v1.events.models import Event, Receipt, ReceiptItem
from api.v1.events.permissions import IsEventParticipants, IsEventOrganizer


class AddEventView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = AddEventSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsEventOrganizer]


class JoinGroupView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = JoinGroupResponseSerializer

    def retrieve(self, request, invite_token=None, *args, **kwargs):
        try:
            event = Event.objects.get(invite_token=invite_token)
        except Event.DoesNotExist:
            return Response(
                {"error": "Мероприятие не найдено"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if event.group:
            event.group.participants.add(request.user)
            return Response(
                {"success": f"Вы присоединились к группе {event.group.name}"},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"error": "У этого мероприятия нет группы"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ReceiptsPositions(RetrieveAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = [IsEventParticipants]


class SelectItemView(RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptNameItemSerializer
    # permission_classes = [IsEventParticipants]
