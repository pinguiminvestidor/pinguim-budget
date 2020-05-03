# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-07 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_remove_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='spent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Expense'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='budget_category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tracker.Budget'),
            preserve_default=False,
        ),
    ]
