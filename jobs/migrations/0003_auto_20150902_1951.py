# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150902_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='name',
            new_name='title',
        ),
    ]
