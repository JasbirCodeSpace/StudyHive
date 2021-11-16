from django import template

register = template.Library()

@register.filter(name='resource_type')
def resource_type(type):
    if type=='Q':
        return "Question paper"
    elif type=='B':
        return "Book"
    elif type=='N':
        return "Notes"