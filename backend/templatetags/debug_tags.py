from django import template
import logging

register = template.Library()

logger = logging.getLogger(__name__)

@register.simple_tag
def debug_print(value):
    print(value)
    logger.debug(value)
    return ''
