from django.contrib import admin
from .models import *


@admin.register(CreditBalance)
class CreditBalanceAdmin(admin.ModelAdmin):
    list_display = ["user","credits","last_updated"]
    search_fields = ["user__email"]
    list_filter = ["last_updated"]



@admin.register(UsageLog)
class UsageLogAdmin(admin.ModelAdmin):
    list_display = ["user","feature","credits_deducted","created_at"]
    search_fields = ["user__email","feature","prompt"]
    list_filter = ["feature","created_at"]
    readonly_fields = ["created_at"]


