from django import template
from urllib.parse import urlencode

register = template.Library()

@register.filter
def is_active(lista):
    return lista.filter(is_active=True) 

@register.filter
def count_is_active(lista):
    return lista.filter(is_active=True).count()

@register.filter
def last_5(lista):
    return lista.filter(is_active=True).order_by('-fecha','-id')[:5]


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()