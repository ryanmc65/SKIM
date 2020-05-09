from django.contrib import admin
from .models import Skim

class SkimAdmin(admin.ModelAdmin):
    display = ('title')

# Register your models here.
admin.site.register(Skim, SkimAdmin)