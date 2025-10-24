from django import forms

class VendaForm(forms.Form):
    quantidade = forms.IntegerField(min_value=1)