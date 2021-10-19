from django.test import TestCase
from trading.models import Instruments, Portfolios, Trades


class TestTradingModels(TestCase):

    def test_instmodel_str(self):
        instrument = Instruments.objects.create(name="TestInstrumentName", symbol="TestSymbol")
        self.assertEqual(str(instrument), "TestInstrumentName")

    def test_portfmodel_str(self):
        portfolio = Portfolios.objects.create(name="TestPortfolioName", description="TestDescription")
        self.assertEqual(str(portfolio), "TestPortfolioName")

    def test_tradesmodel_str(self):
        instrument = Instruments.objects.create(name="TestInstrumentName", symbol="TestSymbol")
        portfolio = Portfolios.objects.create(name="TestPortfolioName", description="TestDescription")
        trade = Trades.objects.create(instrument=instrument, portfolio=portfolio, volume=10)
        self.assertEqual(str(trade), str(instrument) + ', ' + str(portfolio))
