from django.contrib import admin

from .models import *


# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'created', 'updated', 'active',)
    list_filter = ()
    search_fields = ('number', 'name', 'created', 'updated', 'active',)
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class LaneAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'board', 'path', 'created', 'updated', 'active',)
    list_filter = ()
    search_fields = ('number', 'name', 'board', 'path', 'created', 'updated', 'active',)
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class CardAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'land', 'priority', 'created', 'updated', 'active',)
    list_filter = ()
    search_fields = ('number', 'name', 'land', 'priority', 'created', 'updated', 'active',)
    readonly_fields = []

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Priority)
admin.site.register(Board, BoardAdmin)
admin.site.register(Lane, LaneAdmin)
admin.site.register(Card)