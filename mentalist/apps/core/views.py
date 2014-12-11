from django.views.generic import DayArchiveView, TodayArchiveView

from .models import Iteration


class EditionView(object):
    """
    The main printout for the Little Printer. In their documentation they call
    this an `edition`. This lists all the `iterations` for a particular user.
    """
    context_object_name = 'iteration_list'
    template_name = 'base.html'
    date_field = 'date'
    model = Iteration

    def get_queryset(self):
        """
        Retrieve only the `iterations` that belong to a specific user.
        """
        user = self.kwargs.get('user')
        return super().get_queryset().filter(user__username=user)

    def get_context_data(self, **kwargs):
        """
        This has been overridden to give the template access to the amount of
        time it would take to complete all iterations.
        """
        context = super().get_context_data(**kwargs)
        context['total_time'] = self.get_total_time(kwargs['object_list'])
        return context

    def get_total_time(self, iterations):
        """
        Takes a list of iteration instances and returns a string that tells
        you how many minutes it will take to complete them all.
        """
        minutes = sum([i.pearl.minutes for i in iterations])
        total_time = '{} minute'.format(minutes)

        if minutes > 1:
            total_time += 's'

        return total_time


class DayEditionView(EditionView, DayArchiveView):
    """
    Limit the list of returned `iterations` to a specified day.
    """
    allow_future = True


class TodayEditionView(EditionView, TodayArchiveView):
    """
    Limit the list of returned `iterations` to today.
    """
    pass
