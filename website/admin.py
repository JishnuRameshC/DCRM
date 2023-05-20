from django.contrib import admin
from .models import Venue, MyClubeUser, Event

# admin.site.register(Venue)
admin.site.register(MyClubeUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address','phone')
    ordering = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'),'event_date','description','manager')
    list_display = ('name','event_date','venue')
    list_filter = ('venue','event_date')
    ordering = ('event_date',)