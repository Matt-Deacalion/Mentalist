import time
from datetime import date

import schedule
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from apps.core.models import Iteration, LittlePrinter


def print_iterations():
    """
    Send Matt's iterations for today to the Little Printer.
    """
    printer = LittlePrinter.objects.all()[0]
    user = User.objects.get(username='matt')

    iterations = Iteration.objects.filter(pearl__user=user, date=date.today())

    if iterations.exists():
        printer.print_days_iteration(user, date.today())


class Command(BaseCommand):
    help = "Scheduler for printing out a user's daily iterations"

    def handle(self, *args, **options):
        schedule.every().day.at('07:00').do(print_iterations)

        while True:
            schedule.run_pending()
            time.sleep(1)
