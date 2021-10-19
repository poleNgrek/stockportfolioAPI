import graphene
from graphql import GraphQLError
from django.db.models import Q
from .types import InstrumentsType, PortfoliosType, TradesType
from .models import Instruments, Portfolios, Trades
from .mutations import PortfolioCreateMutation, PortfolioUpdateMutation, TradeCreateMutation, TradeUpdateMutation

class Query(graphene.ObjectType):
    all_portfolios = graphene.List(PortfoliosType)
    all_instruments = graphene.List(InstrumentsType)
    all_trades = graphene.List(TradesType)

    search_instruments = graphene.List(InstrumentsType, search=graphene.String())
    instrument = graphene.Field(InstrumentsType, id=graphene.String(), symbol=graphene.String())
    portfolio = graphene.Field(PortfoliosType, id=graphene.String(), name=graphene.String())

    def resolve_search_instruments(root, info, search=None):
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

    def resolve_instrument(root, info, id, symbol):
        if id:
            return Instruments.objects.get(pk=id)
        elif symbol:
            return Instruments.objects.get(symbol=symbol)
        elif id and symbol:
            return Instruments.objects.get(pk=id, symbol=symbol)
        else:
            raise GraphQLError("You must provide id or symbol")

    def resolve_portfolio(root, info, id, name):
        if id:
            return Instruments.objects.get(pk=id)
        elif name:
            return Instruments.objects.get(name=name)
        elif id and name:
            return Instruments.objects.get(pk=id, name=name)
        else:
            raise GraphQLError("You must provide id or name")



class Mutation(graphene.ObjectType):

    create_portfolio = PortfolioCreateMutation.Field()
    update_portfolio = PortfolioUpdateMutation.Field()
    create_trade = TradeCreateMutation.Field()
    update_trade= TradeUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)