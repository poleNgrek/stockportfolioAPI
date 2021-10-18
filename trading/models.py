from django.db import models
from django.utils.translation import gettext_lazy as _

class Instruments(models.Model):
    class Meta:
        verbose_name_plural = 'Instruments'
        verbose_name = 'Instrument'

    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    isEnabled = models.BooleanField()
    type = models.CharField(max_length= 20)
    iexId = models.IntegerField()

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
    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'

    name = models.CharField(max_length=50)
    description = models.TextField()
    holding_value = models.FloatField(null=True)
    total_profit_loss = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Trades(models.Model):
    class Meta:
        verbose_name_plural = 'Trades'
        verbose_name = 'Trade'

    portfolio = models.ForeignKey(Portfolios, to_field='id', on_delete=models.CASCADE)
    instrument = models.ForeignKey(Instruments, to_field='id', on_delete=models.CASCADE)
    volume = models.PositiveIntegerField()
    buy_value = models.PositiveIntegerField()
    sell_value = models.PositiveIntegerField(null=True)
    profit_loss = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s, %s' % ( self.portfolio.name, self.instrument.name)

