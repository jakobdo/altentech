from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def stars(level):
    max_level = 5
    result = []
    # Add stars
    for x in range(level):
        result.append('<i class="material-icons">star</i>')
    for x in range(max_level-level):
        result.append('<i class="material-icons">star_border</i>')
    return mark_safe("\n".join(result))
