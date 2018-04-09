# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agency_company', models.CharField(max_length=10)),
                ('contract_add', models.CharField(max_length=40)),
                ('bank_account', models.CharField(max_length=20)),
                ('subbranch_name', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MediumInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mtitle', models.CharField(max_length=10)),
                ('account_way', models.CharField(default=b'CPC', max_length=3)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReqFundInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req_date', models.CharField(default=b'', max_length=20)),
                ('req_team', models.CharField(max_length=10)),
                ('req_account', models.CharField(default=b'', max_length=20)),
                ('rapplicant', models.CharField(default=b'', max_length=10)),
                ('ramount', models.CharField(default=b'', max_length=5)),
                ('reb_proprotion', models.CharField(default=b'', max_length=10)),
                ('rpay_way', models.CharField(default=b'', max_length=2)),
                ('rpayment_date', models.CharField(default=b'', max_length=20)),
                ('rfund_state', models.CharField(default=b'', max_length=3)),
                ('rauditor', models.CharField(default=b'', max_length=10)),
                ('rmanager', models.CharField(default=b'', max_length=10)),
                ('audit_state', models.CharField(default=b'', max_length=3)),
                ('extend_add', models.CharField(default=b'', max_length=20)),
                ('submit', models.CharField(default=b'', max_length=1)),
                ('isDelete', models.BooleanField(default=False)),
                ('ragent', models.ForeignKey(to='reqfund.AgentInfo', null=True)),
                ('rmedium', models.ForeignKey(to='reqfund.MediumInfo', null=True)),
            ],
        ),
    ]
