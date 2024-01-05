from .models import movie
from django import forms

class Movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','image']