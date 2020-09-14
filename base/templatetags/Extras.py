from django import template
from Post.models import Category

register = template.Library()

def get_categories():
    return Category.objects.all()