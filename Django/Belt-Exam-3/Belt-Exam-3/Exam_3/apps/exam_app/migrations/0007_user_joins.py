# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-29 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0006_auto_20180628_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='joins',
            field=models.ManyToManyField(related_name='_user_joins_+', to='exam_app.User'),
        ),
    ]