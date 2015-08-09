# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_auto_20150808_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sub_category', models.CharField(null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('post_code_in_3', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='store',
            name='area',
            field=models.ForeignKey(to='stores.Area'),
        ),
        migrations.AlterField(
            model_name='store',
            name='city',
            field=models.ForeignKey(to='stores.City'),
        ),
        migrations.AddField(
            model_name='area',
            name='city',
            field=models.ForeignKey(to='stores.City'),
        ),
    ]
