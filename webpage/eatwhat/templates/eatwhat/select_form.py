from django import forms

class selectForm(forms.Form) :
    choices = tuple([(i,i) for i in range(1,13)])
    month = forms.ChoiceField(widget=forms.Select, choices = choices)
