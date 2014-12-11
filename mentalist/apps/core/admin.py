from django.contrib import admin

from .models import LittlePrinter, Pearl, Iteration


class LittlePrinterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
admin.site.register(LittlePrinter, LittlePrinterAdmin)


class PearlAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'answer', 'image', 'minutes')
    list_filter = ('status',)
admin.site.register(Pearl, PearlAdmin)


class IterationAdmin(admin.ModelAdmin):
    list_display = ('pearl', 'user', 'date', 'iteration')
    list_filter = ('user', 'date', 'iteration')
admin.site.register(Iteration, IterationAdmin)
