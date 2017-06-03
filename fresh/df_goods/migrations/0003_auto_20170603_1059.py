# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20170603_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeinfo',
            name='ttitle',
            field=models.CharField(max_length=20),
        ),
    ]
