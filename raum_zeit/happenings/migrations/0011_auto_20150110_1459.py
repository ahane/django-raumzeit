# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0010_auto_20150108_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='happening',
            name='artists',
            field=models.ManyToManyField(to='happenings.Artist', through='happenings.Performance'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='happening',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
    ]
