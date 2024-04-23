from datetime import date
from dateutil import relativedelta

from django import template

register = template.Library()

@register.filter("time_at_club", expects_localtime=True, is_safe=True)
def time_at_club(value):
    time_span = relativedelta.relativedelta(date.today(), value)
    years_spent = time_span.years
    months_spent = time_span.months
    weeks_spent = time_span.weeks
    days_spent = time_span.days

    years_elapsed = ""
    months_elapsed = ""
    weeks_elapsed = ""
    days_elapsed = ""

    if years_spent > 1:
        years_elapsed = f'{years_spent} years'
    
    elif years_spent == 1:
        years_elapsed = f'{years_spent} year'
    
    if months_spent > 1:
        months_elapsed = f'{months_spent} months'
    else:
        months_elapsed = f'{months_spent} month'
    
    if weeks_spent > 1:
        weeks_elapsed = f'{weeks_spent} weeks'
    else:
        weeks_elapsed = f'{weeks_spent} week'

    if days_spent > 1:
        days_elapsed = f'{days_spent} days'
    else:
        days_elapsed = f'{days_spent} day'
    
    #no zero
    if (years_spent > 0 and months_elapsed != 0 and days_elapsed != 0):
        time_spent = f'{years_elapsed}, {months_elapsed}, and {days_elapsed}'

    #single zero
    elif (years_spent == 0 and months_spent != 0 and days_spent != 0):
        time_spent = f'{months_elapsed} and {days_elapsed}'
    elif (years_spent != 0 and months_spent == 0 and days_spent != 0):
        time_spent = f'{years_elapsed} and {days_elapsed}'
    elif (years_spent != 0 and months_spent != 0 and days_spent == 0):
        time_spent = f'{years_elapsed} and {months_elapsed}'
    
    #two zeros
    elif (years_spent == 0 and months_spent == 0 and days_spent != 0):
        time_spent = f'{days_elapsed}'
    elif (years_spent != 0 and months_spent == 0 and days_spent == 0):
        time_spent = f'{years_elapsed}'
    elif (years_spent == 0 and months_spent != 0 and days_spent == 0):
        time_spent = f'{months_elapsed}'
    
    return time_spent

