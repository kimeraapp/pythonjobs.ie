from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass
class memeAdmin*admin.ModelAdmin):
    pass

# Register your models here.
