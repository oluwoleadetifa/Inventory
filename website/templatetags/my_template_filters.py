from django import template

register = template.Library()


@register.filter(name='which_field')
def which_field(field):
    return field.field.__class__.__name__
