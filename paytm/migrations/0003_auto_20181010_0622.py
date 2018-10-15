# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paytm', '0002_auto_20170309_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKNAME',
            field=models.CharField(null=True, max_length=50, blank=True, verbose_name='BANK NAME'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='BANKTXNID',
            field=models.IntegerField(null=True, blank=True, verbose_name='BANK TXN ID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='CURRENCY',
            field=models.CharField(null=True, max_length=4, blank=True, verbose_name='CURRENCY'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='GATEWAYNAME',
            field=models.CharField(null=True, max_length=30, blank=True, verbose_name='GATEWAY NAME'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='ORDERID',
            field=models.CharField(max_length=30, verbose_name='ORDER ID'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='PAYMENTMODE',
            field=models.CharField(null=True, max_length=10, blank=True, verbose_name='PAYMENT MODE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPCODE',
            field=models.IntegerField(verbose_name='RESP CODE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='RESPMSG',
            field=models.TextField(max_length=250, verbose_name='RESP MSG'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='STATUS',
            field=models.CharField(max_length=12, verbose_name='STATUS'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNAMOUNT',
            field=models.FloatField(verbose_name='TXN AMOUNT'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNDATE',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='TXN DATE'),
        ),
        migrations.AlterField(
            model_name='paytmhistory',
            name='TXNID',
            field=models.IntegerField(verbose_name='TXN ID'),
        ),
    ]
