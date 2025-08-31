from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("id","title","landlord","location","price","property_type","is_active","created_at")
    list_filter = ("property_type","is_active","location")
    search_fields = ("title","location","description")