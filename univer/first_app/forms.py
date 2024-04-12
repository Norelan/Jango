from django import forms
from .models import University
 
class ProductForm(forms.Form):
    name = forms.CharField()
    cost = forms.IntegerField()
    univer = forms.ModelChoiceField(queryset=University.objects.all())