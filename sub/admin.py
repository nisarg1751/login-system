from atexit import register
from django.contrib import admin
from sub.models import people
# Register your models here.

@admin.register(people)
class peopleadmin(admin.ModelAdmin):
    list_display = ['id','name','last_name']