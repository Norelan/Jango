from django import forms
from .models import University
 
class ProductForm(forms.Form):
    name = forms.CharField()
    birth = forms.CharField()
    univer = forms.ModelChoiceField(queryset=University.objects.all())
    year = forms.IntegerField()

class UniversityForm(forms.Form):
    name = forms.CharField()
    short_name = forms.CharField()
    year = forms.IntegerField()