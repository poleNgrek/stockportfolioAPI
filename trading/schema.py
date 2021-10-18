import graphene
from django.db.models import Q
from .types import InstrumentsType, PortfoliosType, TradesType
from .models import Instruments, Portfolios, Trades
from .mutations import PortfolioCreateMutation, PortfolioUpdateMutation, TradeCreateMutation, TradeUpdateMutation

class Query(graphene.ObjectType):
    instruments = graphene.List(InstrumentsType, search=graphene.String())

    all_portfolios = graphene.List(PortfoliosType)
    all_instruments = graphene.List(InstrumentsType)
    all_trades = graphene.List(TradesType)

    one_instrument = graphene.Field(InstrumentsType, id=graphene.Int(), symbol=graphene.String())

    def resolve_instruments(root, info, search=None):
        if search:
            filter = (
                Q(id__icontains=search) |
                Q(name__icontains=search) |
                Q(symbol__icontains=search)
            )
            return Instruments.objects.filter(filter)

    def resolve_all_portfolios(root,info):
        return Portfolios.objects.all()

    def resolve_all_instruments(root, info):
        return Instruments.objects.all()

    def resolve_all_trades(root, info):
        return Trades.objects.all()

    def resolve_one_instrument(root, info, id, **kwargs):
        return Instruments.objects.get(pk=id, symbol=kwargs.symbol)


class Mutation(graphene.ObjectType):

    create_portfolio = PortfolioCreateMutation.Field()
    update_portfolio = PortfolioUpdateMutation.Field()
    create_trade = TradeCreateMutation.Field()
    update_trade= TradeUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)