# Generated by Django 3.2.8 on 2021-10-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0005_auto_20211019_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='buy_value',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
