from django.contrib import admin
from .models import Taches

# Register your models here.

class TachesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Taches, TachesAdmin)