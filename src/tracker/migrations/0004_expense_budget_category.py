# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-07 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='budget_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Budget'),
        ),
    ]