from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    surname = 'Mammadov'
    _context = {'date':date, 'name':name, 'surname':surname}
    return render(request, 'home.html', _context)