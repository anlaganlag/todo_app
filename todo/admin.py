from django.contrib import admin
from .models import  TodoItem,BinItem,DoneItem

admin.site.register(TodoItem)
admin.site.register(BinItem)
admin.site.register(DoneItem)


# class TodoItemAdmin(admin.ModelAdmin):
    # formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}

