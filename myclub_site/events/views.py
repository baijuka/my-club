from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar

# Create your views here.

def index(request, year=date.today().year, month=date.today().month):
    month = int(month)
    year = int(year)
    if year < 2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year,month)
    return HttpResponse("<h1>%s</h1><p>%s</p>" % (title,cal))
