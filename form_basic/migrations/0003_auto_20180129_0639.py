# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_basic', '0002_reguser_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('uri', models.URLField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='website_subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(unique=True, max_length=264)),
            ],
        ),
        migrations.AddField(
            model_name='website',
            name='subject',
            field=models.ForeignKey(to='form_basic.website_subject'),
        ),
    ]
