# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='url',
            field=models.CharField(default='asd', max_length=300),
            preserve_default=False,
        ),
    ]
