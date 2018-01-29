# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reguser',
            name='profile_pic',
            field=models.ImageField(upload_to=b'profile_pics', blank=True),
        ),
    ]
