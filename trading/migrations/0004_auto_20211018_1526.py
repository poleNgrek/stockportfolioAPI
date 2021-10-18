# Generated by Django 3.2.8 on 2021-10-18 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0003_auto_20211018_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.instruments'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trading.portfolios'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='profit_loss',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='trades',
            name='sell_value',
            field=models.PositiveIntegerField(null=True),
        ),
    ]