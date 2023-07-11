from django import forms


class TriangleForm(forms.Form):
    cathetus1 = forms.IntegerField(label="Катет 1", min_value=1)
    cathetus2 = forms.IntegerField(label="Катет 2", min_value=1)
