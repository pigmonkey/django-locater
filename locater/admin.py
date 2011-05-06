from django.contrib import admin
from locater.models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'zip')
admin.site.register(Location, LocationAdmin)
