from django.contrib import admin

from .models import Pool
from .models import Transaction


@admin.register(Pool)
class PoolAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ("pool", "user", "amount", "created_at")
