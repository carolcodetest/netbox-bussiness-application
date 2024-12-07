from django.contrib import admin
from .models import BusinessApplication

@admin.register(BusinessApplication)
class BusinessApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'appcode', 'owner', 'delegate', 'servicenow')
    search_fields = ('name', 'appcode', 'owner')
