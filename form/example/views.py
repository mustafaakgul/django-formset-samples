from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import *

from django.core import serializers
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter


def checkbox(request):
    return render(request, 'form1.html')

def studentgender(request):
    if request.method =="POST":
        gender = request.POST.get('gender')
        print(gender)
        searchlist = StudentModel.objects.filter(gender = gender)
        return render(request, "formsearch.html", {"data" : searchlist})
    else:
        studentdisplay = StudentModel.objects.all()
        return render(request, "formsearch.html", {'data' : studentdisplay})

def studentgender1(request):
    if request.method =="POST":
        gender = request.POST.get('gender')
        print(gender)
        searchlist = StudentModel.objects.filter(gender = gender)
        return render(request, "buttonfilter.html", {"data" : searchlist})
    else:
        studentdisplay = StudentModel.objects.all()
        return render(request, "buttonfilter.html", {'data' : studentdisplay})

def loadmoreindex(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Post.objects.filter(title__icontains=q)
    else:
        posts = Post.objects.all()
        # Pagintion
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    posts_obj = paginator.get_page(page_number)
    return render(request, 'loadmore.html', {'posts': posts_obj})

def load_more(request):
    offset=int(request.POST['offset'])
    limit=2
    posts=Post.objects.all()[offset:limit+offset]
    totalData=Post.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })

def colorsname(request):
    result = col.objects.all()
    form = colform(request.POST or None)
    form2 = hideshowshow(request.POST or None)
    form3 = col3form(request.POST or None)
    return render(request, "colorradio.html", {"col" : result, "form" : form, "form2" : form2, "form3" : form3})

def colorsname2(request):
    result = col.objects.all()
    form = colform(request.POST or None)
    form2 = hideshowshow(request.POST or None)
    form3 = col3form(request.POST or None)
    return render(request, "colorradio2.html", {"col" : result, "form" : form, "form2" : form2, "form3" : form3})

def insert(request):
    if request.method =="POST":
        if request.POST.get('chkvalue'):
            savedata = chkboxinsert()
            savedata.coursename = request.POST.get('chkvalue')
            savedata.save()
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def userform(request):
    form = UserForm(request.POST or None)
    return render(request, 'userform.html', {'form' : form})

def playerform1(request):
    form = PlayerForm(request.POST or None)
    return render(request, 'playerform1.html', {'form': form})

def playerform2(request):
    form = PlayerForm2(request.POST or None)
    return render(request, 'playerform2.html', {'form': form})

def searchform(request):
    form = SearchForm(request.POST or None)
    return render(request, 'searchform.html', {'form' : form})

def hideshow(request):
    form = hideshowshow(request.POST or None)
    return render(request, 'hideshowshow.html', {'form': form})
"""
def colorsname(request):
    result = col.objects.all()
    return render(request, "colorradio.html", {"col" : result})"""


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})