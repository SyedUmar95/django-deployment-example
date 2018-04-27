from django import template

register = template.Library()

@register.filter(name='cuts')
def cuts(value,arg):
    """
    This cuts out all the values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cuts',cuts)
