from django.conf.urls import include, patterns, url
from django.contrib import admin

from .views import DayEditionView, TodayEditionView

urlpatterns = patterns(
    '',

    # Examples:
    #
    # /edition/matt/
    # /edition/matt/today/
    url(
        r'^edition/(?P<user>\w+)/(?:today/)?$',
        TodayEditionView.as_view(),
        name='edition_today',
    ),

    # Example:
    #
    # /edition/matt/2014/12/25/
    url(
        r'^edition/(?P<user>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/$',
        DayEditionView.as_view(month_format='%m'),
        name='edition_day',
    ),

    # Example:
    #
    # /edition/matt/2014/dec/25/
    url(
        r'^edition/(?P<user>\w+)/(?P<year>[0-9]{4})/(?P<month>[a-z]{3})/(?P<day>[0-9]{1,2})/$',
        DayEditionView.as_view(),
        name='edition_day_month_name',
    ),

    url(r'^admin/', include(admin.site.urls)),
)
