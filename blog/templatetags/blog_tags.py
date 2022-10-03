from django.template import Library
from django.utils.safestring import mark_safe


register = Library()


@register.filter('safe_html')
def safe_html(text):
    return mark_safe(text)
