# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0003_auto_20150103_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thirdparty',
            name='is_source',
        ),
        migrations.AddField(
            model_name='happeninglink',
            name='identifier',
            field=models.CharField(null=True, blank=True, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='happeninglink',
            name='is_source',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='happeninglink',
            name='happening',
            field=models.ForeignKey(to='happenings.Happening', related_name='links'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='happeninglink',
            name='url',
            field=models.URLField(unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='thirdparty',
            name='url',
            field=models.URLField(unique=True),
            preserve_default=True,
        ),
    ]
