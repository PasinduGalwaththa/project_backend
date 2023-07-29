from django.contrib import admin
from route.models import Route

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('day', 'started_time', 'ended_time')
    list_filter = ('day',)