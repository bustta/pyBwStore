# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_auto_20150823_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='post_code_in_3',
        ),
        migrations.RemoveField(
            model_name='store',
            name='post_code',
        ),
    ]
