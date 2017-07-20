# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_data',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
