# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-22 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_product_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sale',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
