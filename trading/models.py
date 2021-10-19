from django.db import models
from django.utils.translation import gettext_lazy as _

class Instruments(models.Model):
    """The instrument class has a classmethod used to import the data from the json file"""
    class Meta:
        verbose_name_plural = 'Instruments'
        verbose_name = 'Instrument'

    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    isEnabled = models.BooleanField(default=False)
    type = models.CharField(max_length= 20, null=True)
    iexId = models.IntegerField(null=True)

    @classmethod
    def create(cls, **kwargs):
        instrument = cls.objects.create(
            name = kwargs['name'],
            symbol = kwargs['symbol'],
            date = kwargs['date'],
            isEnabled = kwargs['isEnabled'],
            type = kwargs['type'],
            iexId = kwargs['iexId']
        )

        return instrument

    def __str__(self):
        return self.name

class Portfolios(models.Model):
    """A model for the Portfolios. All the fields are nullable to be able to create an empty portfolio."""
    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'

    name = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    holding_value = models.FloatField(null=True)
    total_profit_loss = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Trades(models.Model):
    """The trades model has two foreign keys to the other two models."""
    class Meta:
        verbose_name_plural = 'Trades'
        verbose_name = 'Trade'

    portfolio = models.ForeignKey(Portfolios, to_field='id', on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instruments, to_field='id', on_delete=models.CASCADE)
    volume = models.PositiveIntegerField()
    buy_value = models.PositiveIntegerField(null=True)
    sell_value = models.PositiveIntegerField(null=True)
    profit_loss = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % ( self.instrument.name, self.portfolio.name)

