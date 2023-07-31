from django.contrib import admin
from django.urls import path, include
from . views import *
from django.conf.urls import url


urlpatterns = [
    path('checkbox/', checkbox),
    path('student/', studentgender),
    path('student1/', studentgender1),
    path('loadmore/', loadmoreindex),
    path('load-more',load_more,name='load-more'),
    path('color',colorsname,name='load-more'),
    path('color2',colorsname2,name='load-more2'),
    path('insert', insert, name='load-more'),
    path('userform', userform, name='user-more'),
    path('playerform1', playerform1, name='playerform1-more'),
    path('playerform2', playerform2, name='playerform2-more'),
    path('searchform', searchform, name='playerform2-more'),
    path('hideshow', hideshow, name='hideas-more'),
    url(r'^search/$', search, name='search'),
]
