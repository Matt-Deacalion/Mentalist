from django.contrib import admin

from .models import Iteration, LittlePrinter, OAuth, Pearl


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
    list_display = ('id', 'name', 'subscription_id', 'credentials')
    list_filter = ('credentials',)
    search_fields = ('name',)
admin.site.register(LittlePrinter, LittlePrinterAdmin)


class PearlAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'status', 'answer', 'image', 'minutes')
    list_filter = ('status', 'user',)
admin.site.register(Pearl, PearlAdmin)


class IterationAdmin(admin.ModelAdmin):
    list_display = ('pearl', 'date', 'iteration')
    list_filter = ('date', 'iteration')
admin.site.register(Iteration, IterationAdmin)
