# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_auto_20150823_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='full_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
