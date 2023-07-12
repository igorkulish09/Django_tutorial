from django import forms
from .models import Person


class TriangleForm(forms.Form):
    cathetus1 = forms.IntegerField(label="Катет 1", min_value=1)
    cathetus2 = forms.IntegerField(label="Катет 2", min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]
