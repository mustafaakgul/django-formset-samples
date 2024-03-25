from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<programmer_id>/', views.index, name='index'),
    path('x/<programmer_id>/', views.index2, name='index2'),
    path('x3/<programmer_id>/', views.index3, name='index2'),
]