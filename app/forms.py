from django import forms

from app.models import *

class Schoolform(forms.ModelForm):
    class Meta:
        model=School
        fields='__all__'