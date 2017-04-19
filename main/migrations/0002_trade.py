# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('trade_currency', models.CharField(max_length=10)),
                ('trade_date_signal', models.DateTimeField()),
                ('trade_trend', models.CharField(max_length=6)),
                ('trade_price_open', models.FloatField()),
                ('trade_sl', models.FloatField()),
                ('trade_tp', models.FloatField()),
                ('trade_price_close', models.FloatField()),
                ('trade_date_close', models.DateTimeField()),
                ('trade_result', models.IntegerField()),
            ],
        ),
    ]
