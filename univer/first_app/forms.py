from django import forms
from .models import University
 
class ProductForm(forms.Form):
    name = forms.CharField(label="ФИО")
    birth = forms.CharField(label="Дата рождения")
    univer = forms.ModelChoiceField(queryset=University.objects.all(), label="Университет")
    year = forms.IntegerField(label="Год поступления")

class UniversityForm(forms.Form):
    name = forms.CharField(label="Полное название")
    short_name = forms.CharField(label="Скоращенное название")
    year = forms.IntegerField(label="Год основания")