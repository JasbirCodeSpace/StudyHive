from django import template

register = template.Library()

@register.filter(name='difficulty_level')
def difficulty_level(level):
    if level=='E':
        return "Easy"
    elif level=='M':
        return "Medium"
    elif level=='H':
        return "Hard"