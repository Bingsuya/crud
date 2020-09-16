from django import forms
from .models import ClassBlog

class EditForm(forms.ModelForm):
    class Meta:
        model = ClassBlog
        fields = ['title', 'body']
