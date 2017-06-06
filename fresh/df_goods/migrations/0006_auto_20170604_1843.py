# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0005_cartinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartinfo',
            name='gid',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartinfo',
            name='gs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartinfo',
            name='uid',
            field=models.IntegerField(),
        ),
    ]
