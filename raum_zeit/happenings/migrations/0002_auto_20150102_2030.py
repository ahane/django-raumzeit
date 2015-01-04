# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('links', models.ManyToManyField(to='happenings.Link')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='artist',
            name='links',
            field=models.ManyToManyField(to='happenings.Link'),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='happening',
            old_name='titel',
            new_name='name',
        ),
        migrations.AddField(
            model_name='happening',
            name='artists',
            field=models.ManyToManyField(db_table='performance', to='happenings.Artist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='happening',
            name='links',
            field=models.ManyToManyField(to='happenings.Link'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='happening',
            name='location',
            field=models.ForeignKey(default=1, to='happenings.Location'),
            preserve_default=False,
        ),
    ]
