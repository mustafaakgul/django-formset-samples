from django.shortcuts import render
from . forms import *
from django.forms import formset_factory
from builtins import object
from .models import *

# Create your views here.
def user_profile(request, user_id):
    #user_form = UserProfileaForm()
    user = UserProfile.objects.get(pk = user_id)
    FamilyMemberFormSet = formset_factory(FamilyMemberForm, extra=3)
    #formset = FamilyMemberFormSet()

    if request.method == "POST":
        user_form = UserProfileaForm(request.POST)
        if user_form.is_valid():
            user = UserProfile.objects.create(
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name']
            )
            formset = FamilyMemberFormSet(request.POST)
            if formset.is_valid():
                for form in formset:
                   member = FamilyMember.objects.create(
                       name=form.cleaned_data['name'],
                       relationship=form.cleaned_data['relationship'],
                       user = user
                   )
    else:
        user_form = UserProfileaForm(initial={
            "first_name" : user.first_name,
            "last_name" : user.last_name
        })
        members = FamilyMember.objects.filter(user_id=user.id)
        data = []
        for member in members:
            mem_dict = {
                "name" : member.name,
                "relationship" : member.relationship
            }
            data.append(mem_dict)
        formset = FamilyMemberFormSet(initial=data)

    return render(request, "profile.html", context={"form" : user_form, "formset" : formset, "user":user})


"""
from django.shortcuts import render
from . forms import *
from django.forms import formset_factory
from builtins import object
from .models import *

# Create your views here.
def user_profile(request):
    #user_form = UserProfileaForm()
    FamilyMemberFormSet = formset_factory(FamilyMemberForm, extra=3)
    #formset = FamilyMemberFormSet()

    if request.method == "POST":
        user_form = UserProfileaForm(request.POST)
        if user_form.is_valid():
            user = UserProfile.objects.create(
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name']
            )
            formset = FamilyMemberFormSet(request.POST)
            if formset.is_valid():
                for form in formset:
                   member = FamilyMember.objects.create(
                       name=form.cleaned_data['name'],
                       relationship=form.cleaned_data['relationship'],
                       user = user
                   )
    else:
        user_form = UserProfileaForm()
        formset = FamilyMemberFormSet()

    return render(request, "profile.html", context={"form" : user_form, "formset" : formset})"""