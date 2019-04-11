from django import forms
from .models import Parent, Student

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ('first_name', )