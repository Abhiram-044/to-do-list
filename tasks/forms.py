from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "status", "deadline"]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
        }
