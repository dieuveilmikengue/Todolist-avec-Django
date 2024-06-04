from django.contrib import admin
from .models import Taches

# Register your models here.

class TachesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')


admin.site.register(Taches, TachesAdmin)