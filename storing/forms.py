from django import forms
from storing.models import storingmodel

class storingform(forms.ModelForm):
    class Meta:
        model=storingmodel
        fields='__all__'