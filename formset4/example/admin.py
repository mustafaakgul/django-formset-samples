from django.contrib import admin

# Register your models here.
from .models import Programmer, Language

admin.site.register(Programmer)
admin.site.register(Language)