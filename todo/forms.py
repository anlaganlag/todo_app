
from django import forms
from .models import TodoItem

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = [
            'content',
            'deadline',
            'rating',
            'hours',
        ]