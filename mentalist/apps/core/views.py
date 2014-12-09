from django.views.generic import DayArchiveView, TodayArchiveView

from .models import Iteration


class EditionView(object):
    """
    The main printout for the Little Printer. In their documentation they call
    this an `edition`. This lists all the `iterations` for a particular user.
    """
    date_field = 'date'
    model = Iteration


class DayEditionView(EditionView, DayArchiveView):
    """
    Limit the list of returned `iterations` to a specified day.
    """
    pass


class TodayEditionView(EditionView, TodayArchiveView):
    """
    Limit the list of returned `iterations` to today.
    """
    pass
