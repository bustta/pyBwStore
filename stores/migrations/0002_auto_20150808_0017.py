# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='post_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='telephone',
            field=models.CharField(null=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='store',
            name='website',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
