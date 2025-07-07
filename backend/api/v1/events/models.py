import uuid

from django.contrib.auth import get_user_model
from django.db import models

# from api.v1.receipts.models import Receipt


class ReceiptItem(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название позиции",
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name="Количество",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за единицу",
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Общая сумма",
    )

    event = models.ForeignKey(  # Связь с событием
        "Event",
        on_delete=models.CASCADE,
        related_name="items",
    )


class EventGroup(models.Model):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField(
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    participants = models.ManyToManyField(
        get_user_model(),
        related_name="event_groups",
        blank=True,
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(
        max_length=255,
    )
    organizer = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="organized_events",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    tips_percentage = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
    )
    group = models.ForeignKey(
        EventGroup,
        on_delete=models.CASCADE,
        related_name="events",
        blank=True,
        null=True,
    )
    invite_token = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=True,
        blank=True,
    )
    receipt_image = models.ImageField(
        upload_to="receipts",
        blank=False,
        null=False,
    )
    qr_raw = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
