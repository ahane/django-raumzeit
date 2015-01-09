# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0006_auto_20150105_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='happening',
            name='artists',
        ),
    ]
