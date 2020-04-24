from django.contrib import admin
from .models import  TodoItem,BinItem,DoneItem

admin.site.register(TodoItem)
admin.site.register(BinItem)
admin.site.register(DoneItem)

# Register your models here.
