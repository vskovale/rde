# backend/templatetags/cache_busting.py
from django import template
from django.templatetags.static import static
import time

register = template.Library()

@register.simple_tag
def cache_bust(path):
    url = static(path)
    return f'{url}?v={int(time.time())}'
