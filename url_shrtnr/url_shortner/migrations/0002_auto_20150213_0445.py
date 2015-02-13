# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_short', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltable',
            name='shortened_url',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
