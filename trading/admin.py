from django.contrib import admin
from .models import Instruments, Portfolios, Trades

class InstrumentsAdmin(admin.ModelAdmin):
    model = Instruments

    list_display = [
        'id',
        'name',
        'symbol',
        'date',
        'isEnabled',
        'type',
        'iexId',
    ]

class PortfoliosAdmin(admin.ModelAdmin):
    model = Portfolios

    list_display = [
        'id',
        'name',
        'description',
        'holding_value',
        'total_profit_loss',
    ]

class TradesAdmin(admin.ModelAdmin):
    model = Trades

    list_display = [
        'id',
        'portfolio',
        'instrument',
        'volume',
        'buy_value',
        'sell_value',
        'profit_loss',
    ]

admin.site.register(Instruments, InstrumentsAdmin)
admin.site.register(Portfolios, PortfoliosAdmin)
admin.site.register(Trades, TradesAdmin)