from django import template

register = template.Library()

@register.filter
def zip(list1, list2):
    return zip(list1, list2)


@register.filter(name='subtract')
def subtract(value, arg):
    return float(value) - float(arg)