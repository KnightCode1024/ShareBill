import uuid

from django.contrib.auth import get_user_model
from django.db import models


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

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Мероприятие",
    )
    owners = models.ManyToManyField(
        get_user_model(),
        blank=True,
        related_name="owners",
        verbose_name="Владелец позиции",
    )


class Receipt(models.Model):
    total = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        null=True,
        verbose_name="Общая сумма",
    )
    qr_raw = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Сырой чек",
    )
    items = models.ManyToManyField(
        ReceiptItem,
        blank=True,
        verbose_name="Позиции",
    )
    receipt_img = models.ImageField(
        verbose_name="Фото чека",
        blank=True,
        null=True,
    )


class EventGroup(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название группы",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    participants = models.ManyToManyField(
        get_user_model(),
        related_name="event_groups",
        blank=True,
        verbose_name="Участники",
    )


class Event(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название мероприятия",
    )
    organizer = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="organized_events",
        verbose_name="Огранизатор мероприятия",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Создано в"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активен",
    )
    tips = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name="Чаевые",
    )
    group = models.ForeignKey(
        EventGroup,
        on_delete=models.CASCADE,
        related_name="group",
        blank=True,
        null=True,
        verbose_name="Группа",
    )
    invite_token = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Код приглашения",
    )

    receipt = models.OneToOneField(
        Receipt,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="receipt",
        verbose_name="Чек",
    )
