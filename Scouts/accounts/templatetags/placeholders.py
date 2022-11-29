from django import template

register = template.Library()


@register.filter
def placeholder(field, text):
    field.field.widget.attrs['placeholder'] = text
    return field
