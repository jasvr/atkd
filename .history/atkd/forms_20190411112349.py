from django import forms
from .models import Parent, Student

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ('first_name','last_name')

class SForm(forms.ModelForm):
    
    class Meta:
        model = Song
        fields = ('title', 'album', 'preview_url', 'artist',)