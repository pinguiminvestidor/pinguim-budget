# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Aggregation
from django.db.models import Sum

# Create your models here.

class Expense(models.Model):
    '''
    An expense row classified as defined by our spreadsheet.

    Short description, free text
    Category, chosen from a pre-fixed list
    Value cost in money units (using yen now)
    Date recorded (defaulting to today)
    '''

    description = models.CharField(max_length=255)
    day = models.DateField(default=timezone.now)
    cost = models.IntegerField()

    # Category as FK:
    budget_category = models.ForeignKey('Budget', on_delete=models.CASCADE)

    # From "Your Money or Your Life"
    fulfillment = models.IntegerField(default=0, help_text="Between -1 and 1")

    comment = models.TextField(blank=True, help_text="Elaborate on what was spent on")

    # this differs "active" transactions from "inactive" ones that are older than this month
    active = models.BooleanField(default=True, editable=False)


    def __unicode__(self):
        return self.description

class Budget(models.Model):
    '''
    A representation of an allocated budget category, with its limit imposed.
    '''

    name = models.CharField(max_length=100)
    amount  = models.IntegerField()
    
    def total_spent(self):
        '''
        Sums up everything that was spent for this category, which will then be used to turn
        into a property.
        '''

        total = Expense.objects.filter(budget_category__name = self.name, active = True).aggregate(total_spent=Sum('cost'))['total_spent']

        if total is None:
            return 0
        else:
            return total

    def net_fulfillment(self):
        '''
        Sum all the fulfillment gained on the active expenses in order to see
        whether you have been really getting the happiness you wish for your
        money spent.

        Thanks, Vicki Robins!
        '''
        total = Expense.objects.filter(budget_category__name = self.name, active = True).aggregate(net_fulfillment=Sum('fulfillment'))['net_fulfillment']
        if total is None:
            return 0
        else:
            return total

    # Calculate Remaining Budget:
    def balance(self):
        res = (self.amount - self.total_spent())
        return res

    def percent_left(self):
        perc = 1.0 - float(self.total_spent()) / self.amount
        if perc <= 0:
            return "{0:.0%}".format(0)
        else:
            return "{0:.0%}".format(perc)

    def status(self):
        try:
            perc = float(self.total_spent()) / self.amount
        except ZeroDivisionError:
            perc = 0
        if perc < .7:
            return "OK"
        elif .7 < perc < .9:
            return "Warning"
        elif .9 < perc < 1:
            return "Critical"
        else:
            return "Budget blown"

    def __unicode__(self):
        return self.name

class NetWorth(models.Model):
    '''
    A "line in my complete net worth calculation spreadsheet, including:
     - Cash Positions
     - Assets
     - Calculations of percentage of goal achieved
     - Estimation of total passive income

    Some of the columns will be read-only, calculated on the fly.
    '''

    # Date of Portfolio statement
    day = models.DateField(default=timezone.now)

    # Cash Positions
    cash_brazil = models.FloatField(default=0)
    savings_brazil = models.FloatField(default=0)
    cash_japan = models.FloatField(default=0)
    usd_reserve = models.FloatField(default=0)

    # Assets
    other_fixed_income = models.FloatField(default=0)
    tesouro_direto = models.FloatField(default=0)
    FII = models.FloatField(default=0)
    acoes = models.FloatField(default=0)
    stocks = models.FloatField(default=0)

    # Calculated values:
    def total(self, forShow=True):
        subtotal = (
                self.cash_brazil +
                self.savings_brazil +
                self.cash_japan +
                self.usd_reserve +
                self.other_fixed_income +
                self.tesouro_direto +
                self.FII +
                self.acoes +
                self.stocks
               )
        if forShow:
            return '{:,}'.format(subtotal)
        else:
            return subtotal

    def total_cash(self):
        subtotal = self.cash_brazil + self.savings_brazil + self.cash_japan + self.usd_reserve
        return '{:,}'.format(subtotal)

    def total_fixed_income(self):
        subtotal = self.other_fixed_income + self.tesouro_direto
        return '{:,}'.format(subtotal)

    def total_equity(self):
        subtotal = self.FII + self.acoes + self.stocks
        return '{:,}'.format(subtotal)

    def percent_of_goal(self):
        perc = self.total(forShow=False) / 2700000.0
        return '{0:.2%}'.format(perc)

    # TODO: how can we calculate the delta between the previous date?

    def passive_income_projection(self):
        return self.total() / 100.0

    # name of this object:
    def __unicode__(self):
        return unicode('Snapshot ' + str(self.id))
