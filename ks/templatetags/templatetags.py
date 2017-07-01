from django import template

register = template.Library()


@register.filter(name="add1")
def add1(value):
    return int(value) + 1


