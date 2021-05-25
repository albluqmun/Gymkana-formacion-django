from django.contrib import admin

from .models import Event, New

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'start_date','end_date')
admin.site.register(Event, EventAdmin)



class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'publish_date')
admin.site.register(New, NewAdmin)
