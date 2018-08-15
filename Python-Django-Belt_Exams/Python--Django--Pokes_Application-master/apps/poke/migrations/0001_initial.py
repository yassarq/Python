# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poke',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateField(null=True)),
                ('counter', models.IntegerField(null=True, default=0)),
                ('total', models.IntegerField(null=True, default=0)),
            ],
            options={
                'db_table': 'poke',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.TextField(null=True, max_length=20)),
                ('last_name', models.TextField(null=True, max_length=20)),
                ('email', models.TextField(null=True, max_length=20)),
                ('description', models.TextField(null=True, max_length=500)),
                ('password', models.TextField(null=True, max_length=20)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='poke',
            name='poked',
            field=models.ForeignKey(to='poke.User', related_name='pokedpokes'),
        ),
        migrations.AddField(
            model_name='poke',
            name='poker',
            field=models.ForeignKey(to='poke.User', related_name='pokerpokes'),
        ),
    ]
