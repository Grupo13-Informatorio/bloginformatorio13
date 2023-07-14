from django import template

register = template.Library()

@register.filter
def is_active(lista):
    return lista.filter(is_active=True) 

@register.filter
def count_is_active(lista):
    return lista.filter(is_active=True).count()