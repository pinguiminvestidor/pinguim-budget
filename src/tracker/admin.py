# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Expense, Budget

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'budget_category',
        'cost',
        'fulfillment',
        'day',
    )
    ordering = ['-day', 'cost']
    list_filter = ['day', 'budget_category']

class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'amount',
        'total_spent',
        'balance',
        'percent_left',
        'net_fulfillment',
        'status',
    )
    ordering = ['name']

class ExpenseInline(admin.TabularInline):
    model = Expense
    extra = 0

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Budget, BudgetAdmin)
