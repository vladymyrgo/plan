from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Dream, Task


class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        widgets = {
            'completion_date': SelectDateWidget,
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {
            'start_date': SelectDateWidget,
            'end_date': SelectDateWidget,
        }
