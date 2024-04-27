from django.contrib import admin

from .models import GymSession
from .models import GymSessionImage


class GymSessionImageInline(admin.TabularInline):
    model = GymSessionImage
    extra = 1


@admin.register(GymSession)
class GymSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "note")
    inlines = [GymSessionImageInline]


@admin.register(GymSessionImage)
class GymSessionImageAdmin(admin.ModelAdmin):
    list_display = ("session", "image", "upload_date")
