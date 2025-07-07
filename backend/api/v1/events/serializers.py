from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.v1.events.models import EventGroup, Event, ReceiptItem
from api.v1.events.utils import (
    decode_qr_code_from_image,
    get_receipt_info_by_qr_raw,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "photo",
        ]


class EventGroupSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = EventGroup
        fields = "__all__"


class AddEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        img = validated_data["receipt_image"]
        qr_raw = decode_qr_code_from_image(img)
        receipt_data = get_receipt_info_by_qr_raw(qr_raw)

        if (
            not receipt_data
            or receipt_data.get("code") != 1
            or "data" not in receipt_data
        ):
            raise serializers.ValidationError(
                "Не удалось получить данные чека"
            )

        json_data = receipt_data["data"]["json"]

        event = Event.objects.create(
            name=validated_data["name"],
            receipt_image=img,
            qr_raw=qr_raw,
            organizer=user,
            total_amount=json_data["totalSum"] / 100,
        )

        if not event.group:
            group = EventGroup.objects.create(name=event.name)
            group.participants.add(user)
            event.group = group
            event.save()

        if "items" in json_data:
            for item in json_data["items"]:
                ReceiptItem.objects.create(
                    name=item["name"],
                    price=item["price"] / 100,
                    quantity=item["quantity"],
                    total=item["sum"] / 100,
                    event=event,
                )

        return event


class ReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = ["name", "quantity", "price", "total"]

    class Meta:
        model = Event
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    group = EventGroupSerializer()
    receipt_items = ReceiptItemSerializer(many=True, read_only=True)
    organizer = UserSerializer()

    class Meta:
        model = Event
        fields = "__all__"


class JoinGroupResponseSerializer(serializers.Serializer):
    success = serializers.CharField(required=False)
    error = serializers.CharField(required=False)
