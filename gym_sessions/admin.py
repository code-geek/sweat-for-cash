from django.contrib import admin

from .models import GymSession
from .models import GymSessionImage


@admin.register(GymSession)
class GymSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "note")


@admin.register(GymSessionImage)
class GymSessionImageAdmin(admin.ModelAdmin):
    """Admin View for GymSessionImage"""

    list_display = ("session", "image", "upload_date")
