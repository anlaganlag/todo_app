from django import template

register = template.Library()

from todo.models import BinItem,DoneItem,TodoItem

@register.simple_tag
def  total_binitem():
    return BinItem.objects.count()


@register.simple_tag
def  total_doneitem():
    return DoneItem.objects.count()

@register.simple_tag
def  total_todoitem():
    return TodoItem.objects.count()
