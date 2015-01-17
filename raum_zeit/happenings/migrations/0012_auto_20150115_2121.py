# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0011_auto_20150110_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='happening',
            options={'ordering': ('start', 'stop')},
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='name',
            field=models.CharField(max_length=200, unique=True),
            preserve_default=True,
        ),
    ]
