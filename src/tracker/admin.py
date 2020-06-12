from django.contrib import admin
from tracker.models import Expense, Budget, NetWorth

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

class NetWorthAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'total_cash',
        'total_fixed_income',
        'total_equity',
        'total',
        'percent_of_goal',
    )
    ordering = [ '-day' ]

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Budget, BudgetAdmin)
admin.site.register(NetWorth, NetWorthAdmin)
