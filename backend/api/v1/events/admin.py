from django.contrib import admin

from api.v1.events.models import ReceiptItem, EventGroup, Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(EventGroup)
class EventGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(ReceiptItem)
class ReceiptItemAdmin(admin.ModelAdmin):
    pass
