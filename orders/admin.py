from django.contrib import admin
from .models import Order


@admin.register(Order)
class Orderdmin(admin.ModelAdmin):
    list_display = ('order_identificator', 'status', 'created_at',)
    list_filter = ('created_at',)
    list_display_links = ('order_identificator',)
    search_fields = ('order_identificator',)
    prepopulated_fields = {'slug': ('order_identificator',)}
    readonly_fields = ["commentary", "payment_method"]