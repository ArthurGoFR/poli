# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-12 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gdpcore', '0002_auto_20160412_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='second_left_prop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_second_left_prop', to='gdpcore.Proposition'),
        ),
    ]