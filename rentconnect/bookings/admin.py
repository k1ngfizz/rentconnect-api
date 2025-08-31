from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BookingRequest

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ("id","user","property","status","created_at")
    list_filter = ("status",)
    search_fields = ("user__username","property__title")