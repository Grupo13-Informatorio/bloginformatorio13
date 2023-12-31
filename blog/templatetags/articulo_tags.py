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

@register.filter
def si_no(booleano):
    if booleano:
        return "Activo"
    else:
        return "Suspendido"
    
@register.filter
def rol(usuario):
    if usuario.is_superuser:
        return "Administrador"
    elif usuario.is_miembro:
        return "Colaborador"
    else:
        return "Visitante"


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()