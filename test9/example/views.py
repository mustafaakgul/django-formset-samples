from django.shortcuts import render, redirect
from .models import Programmer, Language
from django.forms import modelformset_factory, inlineformset_factory

def index(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    #LanguageFormset = modelformset_factory(Language, fields=('name',))
    LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name',), can_delete=True, extra=1, max_num=6)

    if request.method == 'POST':
        #formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = LanguageFormset(request.POST, instance=programmer)
        if formset.is_valid():
            formset.save()
            #instances = formset.save(commit=False)
            #for instance in instances:
            #    instance.programmer_id = programmer.id
            #    instance.save()

            return redirect('index', programmer_id=programmer.id)

    #formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = LanguageFormset(instance=programmer)

    return render(request, 'index.html', {'formset' : formset})

def index2(request, programmer_id):  #only see
    programmer = Programmer.objects.get(pk=programmer_id)
    LanguageFormset = modelformset_factory(Language, fields=('name',))

    formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))

    return render(request, 'index2.html', {'formset' : formset})

def index3(request, programmer_id):  #only see
    programmer = Programmer.objects.get(pk=programmer_id)
    LanguageFormset = modelformset_factory(Language, fields=('name',))

    if request.method == 'POST':
        formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
               instance.programmer_id = programmer.id
               instance.save()
            return redirect('index3', programmer_id=programmer.id)
    formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))

    return render(request, 'index3.html', {'formset' : formset})
"""
def index(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    #LanguageFormset = modelformset_factory(Language, fields=('name',))
    LanguageFormset = inlineformset_factory(Programmer, Language, fields=('name',))

    if request.method == 'POST':
        #formset = LanguageFormset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = LanguageFormset(request.POST, instance=programmer)
        if formset.is_valid():
            formset.save()
            #instances = formset.save(commit=False)
            #for instance in instances:
            #    instance.programmer_id = programmer.id
            #    instance.save()

            return redirect('index', programmer_id=programmer.id)

    #formset = LanguageFormset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = LanguageFormset(instance=programmer)

    return render(request, 'index.html', {'formset' : formset})
"""