# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0003_auto_20170603_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeinfo',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
    ]
