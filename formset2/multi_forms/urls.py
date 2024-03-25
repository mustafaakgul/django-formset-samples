
from django.conf.urls import url
from django.urls import path

from multi_forms import views

app_name = "multi_forms"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("list/", views.list, name="list"),
]