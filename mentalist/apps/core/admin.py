from django.contrib import admin

from .models import LittlePrinter, Pearl, Iteration


class LittlePrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
admin.site.register(LittlePrinter, LittlePrinterAdmin)


class PearlAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'text', 'answer', 'image', 'minutes')
admin.site.register(Pearl, PearlAdmin)


class IterationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pearl', 'date', 'iteration')
    list_filter = ('user', 'pearl', 'date')
admin.site.register(Iteration, IterationAdmin)
