# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0009_auto_20150108_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='happening',
            name='description',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
