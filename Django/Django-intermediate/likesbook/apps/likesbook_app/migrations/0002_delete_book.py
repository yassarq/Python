# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 20:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likesbook_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]