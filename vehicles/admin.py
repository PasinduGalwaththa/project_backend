from django.contrib import admin
from vehicles.models import vehicles

class RouteInline(admin.TabularInline):
    model = vehicles.routes.through 

@admin.register(vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('vehiclenumber', 'drivername', 'routename', 'collector',)
    inlines = [RouteInline] 