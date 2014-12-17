from django.contrib import admin

from .models import OAuth, LittlePrinter, Pearl, Iteration


class OAuthAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'client_key',
        'client_secret',
        'resource_owner_key',
        'resource_owner_secret',
    )
    search_fields = ('name',)
admin.site.register(OAuth, OAuthAdmin)


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
