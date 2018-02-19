from django import forms

class ApptForm(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'class':'form-control'}))
    time = forms.TimeField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'class':'form-control'}))
