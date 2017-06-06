# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0004_typeinfo_isdelete'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField(max_length=20)),
                ('gid', models.IntegerField(max_length=20)),
                ('gs', models.IntegerField(max_length=20)),
            ],
            options={
                'db_table': 'cartinfo',
            },
        ),
    ]
