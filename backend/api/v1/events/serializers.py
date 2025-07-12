from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.v1.events.models import EventGroup, Event, ReceiptItem, Receipt
from api.v1.events.utils import (
    decode_qr_code_from_image,
    get_receipt_info_by_qr_raw,
)


class ReceiptItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptItem
        fields = [
            "name",
            "quantity",
            "price",
            "total",
            "owners",
        ]


class ReceiptSerializer(serializers.ModelSerializer):
    items = ReceiptItemSerializer(many=True)

    class Meta:
        model = Receipt
        fields = [
            "id",
            "total",
            "items",
            "receipt_img",
        ]


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
        fields = [
            "name",
            "created_at",
            "participants",
        ]


class AddEventSerializer(serializers.ModelSerializer):
    receipt_img = serializers.ImageField(write_only=True)

    class Meta:

        model = Event
        fields = [
            "name",
            "tips",
            "group",
            "receipt_img",
        ]

    def create(self, validated_data):
        user = self.context["request"].user
        img = validated_data.pop("receipt_img")
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

        receipt = Receipt.objects.create(
            total=json_data["totalSum"] / 100,
            qr_raw=qr_raw,
            receipt_img=img,
        )

        event = Event.objects.create(
            name=validated_data["name"],
            organizer=user,
            receipt=receipt,
        )

        if not event.group:
            group = EventGroup.objects.create(name=event.name)
            group.participants.add(user)
            event.group = group
            event.save()

        if "items" in json_data:
            for item in json_data["items"]:
                receipt_item = ReceiptItem.objects.create(
                    name=item["name"],
                    price=item["price"] / 100,
                    quantity=item["quantity"],
                    total=item["sum"] / 100,
                    event=event,
                )
                receipt.items.add(receipt_item)

        return event


class EventSerializer(serializers.ModelSerializer):
    group = EventGroupSerializer()
    organizer = UserSerializer()
    receipt = ReceiptSerializer()

    class Meta:
        model = Event
        fields = [
            "name",
            "organizer",
            "created_at",
            "is_active",
            "tips",
            "group",
            "invite_token",
            "receipt",
        ]


class JoinGroupResponseSerializer(serializers.Serializer):
    success = serializers.CharField(required=False)
    error = serializers.CharField(required=False)


class SelectItemSerializer(serializers.ModelSerializer):
    pass


class ReceiptItemForNameSerializer(serializers.Serializer):
    class Meta:
        model = ReceiptItem
        fields = [
            "name",
        ]


class ReceiptNameItemSerializer(serializers.ModelSerializer):
    items = ReceiptItemForNameSerializer(many=True)

    class Meta:
        model = Receipt
        fields = [
            "items",
        ]
