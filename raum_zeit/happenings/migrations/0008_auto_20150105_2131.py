# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0007_remove_happening_artists'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('kind', models.CharField(max_length=4, default='DJ', choices=[('LIVE', 'Live Music'), ('LIDJ', 'Live Set'), ('DJ', 'Set')])),
                ('artist', models.ForeignKey(related_name='performances', to='happenings.Artist')),
                ('happening', models.ForeignKey(related_name='performances', to='happenings.Happening')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='performance2',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='performance2',
            name='happening',
        ),
        migrations.RemoveField(
            model_name='happening',
            name='artists2',
        ),
        migrations.DeleteModel(
            name='Performance2',
        ),
        migrations.AddField(
            model_name='happening',
            name='artists',
            field=models.ManyToManyField(blank=True, to='happenings.Artist', through='happenings.Performance'),
            preserve_default=True,
        ),
    ]
