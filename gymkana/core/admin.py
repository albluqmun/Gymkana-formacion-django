from django.contrib import admin
from .models import New, Event

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'publish_date')
    list_filter = ('publish_date',)
    search_fields = ('title', 'subtitle')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title', 'subtitle')
