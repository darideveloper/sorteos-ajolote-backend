from . import models
from django.contrib import admin

@admin.register (models.Lottery)
class LotteryAdmin (admin.ModelAdmin):
    list_display = ('name', 'created_at', 'numbers', 'total_price', 'is_open')
    list_filter = ('created_at', 'is_open')
    list_per_page = 20

@admin.register (models.Ticket)
class TicketAdmin (admin.ModelAdmin):
    list_display = ('lottery', 'number', 'buyer_name', 'buy_at', 'is_paid', 'active')
    list_filter = ('lottery', 'buy_at', 'is_paid', 'active')
    search_fields = ('lottery__name', 'number', 'buyer_name', 'buyer_email')
    search_help_text = "Puedes buscar por nombre del sorteo, número de boleto, nombre del comprador y correo electrónico del comprador"
    list_per_page = 20