from django import template
from django.utils.timezone import now
from ..utils import bizzfuzz

register = template.Library()


@register.filter(name='bizz')
def bizz(val):
    return bizzfuzz(val)


@register.filter(name='eligible')
def eligible(val):
    years = to_age(val)
    return 'allowed' if years > 13 else 'blocked'


def to_age(val):
    today = now()
    if today.month < val.month or (today.month == val.month and today.day < val.day):
        return today.year - val.year - 1
    else:
        return today.year - val.year