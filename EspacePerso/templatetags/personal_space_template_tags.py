from django import template
from django.template.defaultfilters import stringfilter
"""
register = template.Library

@register.filter()
@stringfilter
def non_null_or_empty(value):
    replacement = "Non renseigné !"
    if value == "" :
        return value.replace("", replacement)
    elif value == "NONE":
        return value.replace("NULL", replacement)"""