from django import template

register = template.Library()

@register.filter(name = 'rep')
def rep(value,arg):
    return value.replace(arg,'#')
