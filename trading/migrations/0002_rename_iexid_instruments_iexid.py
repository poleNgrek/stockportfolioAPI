# Generated by Django 3.2.8 on 2021-10-15 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instruments',
            old_name='iexID',
            new_name='iexId',
        ),
    ]
