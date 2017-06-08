# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0007_orderinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='ispay',
            field=models.BooleanField(default=False),
        ),
    ]
