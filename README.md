# Personal budgeting and expenses app with the Django framework

This is the way I track and control my expenses every day. Written from scratch and originally a study on how to build things over the Django Framework, this is now a full-fledged application that allows you to set up budgets, adjust them, and calculate automatically the remaining budget for the month.

Probably not the best way for a beginner in personal finance to do it, but if you're adventurous enough, do give it a go!

## Requirements

 - Python3
 - A recent version of Django
 - `pip` and `virtualenv`
 - Standard Linux utils, I guess?

## Install instructions

Install `pip` and `virtualenv` through your distro's package management if you haven't done it already. Ubuntu/Debian example:

    sudo apt-get install python-pip virtualenv

Create a virtual python environment:

    virtualenv Django-env

Activate the virtual environment:

    cd Django-env
    source bin/activate

Install Django locally through pip:

    pip install django

Copy this repo's `src` folder into this environment:

    mkdir budget
    cp -r pinguim-budget/src/* budget/

Create required Django models to start the application:

    cd budget
    ./manage.py migrate

Launch application using test server:

    ./manage.py runserver

The app should be available by pointing the browser to http://localhost:8000

## Credits

For more excellent content concerning personal finance and investments (in Portuguese), please see:

 - Pinguim Investidor's Main Website: https://pinguiminvestidor.com
 - Twitter account: [@pinguiminvest](https://twitter.com/pinguiminvest)
 - Facebook Page: https://facebook.com/pinguiminvest
