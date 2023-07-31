from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.forms.widgets import SelectDateWidget
from .models import *

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'))
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    email= forms.EmailField()
    age= forms.IntegerField()
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    birth_year = DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    gender = ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES)
    favorite_colors = forms.MultipleChoiceField(required=False,
                                                widget=CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'special'}))
    url = forms.URLField()
    comment = forms.CharField(
        widget=forms.TextInput(attrs={'size': '40'}))

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name']
        widgets = {'name': forms.HiddenInput()}

class PlayerForm2(forms.Form):
    name = forms.CharField(widget=forms.HiddenInput())

class SearchForm(forms.Form):
    type = forms.ChoiceField(choices=FRUIT_CHOICES)

class hideshowshow(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["available"]

class colform(forms.ModelForm):
    class Meta:
        model = col
        exclude = ["colorname"]

class col3form(forms.Form):
    cname = forms.CharField()
    cplusname = forms.CharField()
    javaname = forms.CharField()
    pythonname = forms.CharField()
