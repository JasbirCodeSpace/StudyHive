from django import template
import datetime

register = template.Library()

@register.filter(name='difficulty_level')
def difficulty_level(level):
    if level=='E':
        return "Easy"
    elif level=='M':
        return "Medium"
    elif level=='H':
        return "Hard"

@register.filter
def timestamp(value):
    return datetime.datetime.fromtimestamp(value).strftime("%d %b %Y %I:%M:%S")

@register.filter
def duration(value):
    return str(datetime.timedelta(seconds = value))