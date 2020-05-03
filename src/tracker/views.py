# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def summary(request):
    '''
    Renders the default summary dashboard to people.
    '''
    return HttpResponse("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Django Expenses app by Pinguim Investidor</title>
        <meta http-equiv="Content-Type" value="text/html; charset=utf-8" />
    </head>
    <body>
        <header>
            <h1>Django Expenses App</h1>
            <p>
                By Pinguim Investidor
            </p>
        </header>
        <p>
            Hi. There will (eventually) be something here, like reports, etc.
            But right now you're better off going to the Admin page and adjusting the stuff yourself.
        </p>
        <p>
            Looking for the <a href="/admin">admin</a> page?
        </p>
    </body>
</html>
    """)
