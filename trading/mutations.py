import graphene
from .types import PortfoliosType, TradesType
from .models import Instruments, Portfolios, Trades

class PortfolioCreateMutation(graphene.Mutation):
    """A mutation which allows the creation of a new Portfolio"""

    class Arguments:
        name = graphene.String(required=False)
        description = graphene.String(required=False)

    portfolio = graphene.Field(PortfoliosType)

    @classmethod
    def mutate(cls, root, info, name="", description=""):
        if name and description:
            portfolio = Portfolios(name=name, description=description)
        elif name:
            portfolio = Portfolios(name=name)
        elif description:
            portfolio = Portfolios(description=description)
        else:
            portfolio = Portfolios()
            
        portfolio.save()
        
        return PortfolioCreateMutation(portfolio=portfolio)

class PortfolioUpdateMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    portfolio = graphene.Field(PortfoliosType)

    @classmethod
    def mutate(cls, root, info, id, name, description):
        portfolio = Portfolios.objects.get(id=id)
        portfolio.name = name
        portfolio.description = description
        portfolio.save()
        
        return PortfolioUpdateMutation(portfolio=portfolio)

class TradeCreateMutation(graphene.Mutation):

    class Arguments:
        portfolio = graphene.ID(required=True)
        instrument = graphene.ID(required=True)
        volume = graphene.Int(required=True)
        bvalue = graphene.Int(required=True)
        svalue = graphene.Int(required=True)

    trade = graphene.Field(TradesType)

    @classmethod
    def mutate(cls, root, info, portfolio, instrument, volume, bvalue, svalue):
        portfolio = Portfolios.objects.get(id=portfolio)
        instrument = Instruments.objects.get(id=instrument)
        trade = Trades(portfolio=portfolio, instrument=instrument, volume=volume,buy_value=bvalue, sell_value=svalue)
        trade.save()
        
        return TradeCreateMutation(trade=trade)

class TradeUpdateMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID(required=True)
        portfolio = graphene.Int(required=True)
        instrument = graphene.Int(required=True)
        volume = graphene.Int(required=True)
        bvalue = graphene.Int(required=True)
        svalue = graphene.Int(required=True)

    trade = graphene.Field(TradesType)

    @classmethod
    def mutate(cls, root, info, id, portfolio, instrument, volume, bvalue, svalue):
        trade = Trades.objects.get(id=id)
        trade.portfolio = Portfolios.objects.get(id=portfolio)
        trade.instrument = Instruments.objects.get(id=instrument)
        trade.volume = volume
        trade.buy_value = bvalue
        trade.sell_value = svalue
        trade.save()
        
        return TradeUpdateMutation(trade=trade)
