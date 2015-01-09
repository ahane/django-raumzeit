# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0008_auto_20150105_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistlink',
            name='identifier',
            field=models.CharField(help_text='The id used at the third party', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='happeninglink',
            name='identifier',
            field=models.CharField(help_text='The id used at the third party', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='locationlink',
            name='identifier',
            field=models.CharField(help_text='The id used at the third party', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
