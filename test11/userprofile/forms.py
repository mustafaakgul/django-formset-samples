from django import forms

class UserProfileaForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

class FamilyMemberForm(forms.Form):
    name = forms.CharField(max_length=50)
    relationship = forms.CharField(max_length=50)
