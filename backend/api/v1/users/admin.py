from django.contrib import admin
from api.v1.users.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
