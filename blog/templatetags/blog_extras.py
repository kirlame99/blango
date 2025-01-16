from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()

@register.filter(name="author_details")
def author_details(author,current_user=None):
  if not isinstance(author, user_model):
    # return empty string as safe default
    return ""
  if author == current_user:
    return format_html("<strong>me</strong>")
  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = author.username
  if author.email:
    return format_html('<a href="{}">{}</a>',author.email,name)
  else:
    return format_html('{}',name)

