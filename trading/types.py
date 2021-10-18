from graphene_django.types import DjangoObjectType
from .models import Instruments, Portfolios, Trades

class InstrumentsType(DjangoObjectType):
    class Meta:
        model = Instruments
        #fields = ("id","name", "symbol", "date", "isEnabled", "type", "iexId")
        fields = "__all__"

class PortfoliosType(DjangoObjectType):
    class Meta:
        model = Portfolios
        #fields = ("id", "name", "description", "holding_value", "total_profit_loss", "created_at", "last_modified")
        fields = "__all__"

class TradesType(DjangoObjectType):
    class Meta:
        model = Trades
        #fields = ("id", "portfolio", "instrument", "volume", "buy_value", "sell_value", "profit_loss", "created_at", "last_modified")
        fields = "__all__"