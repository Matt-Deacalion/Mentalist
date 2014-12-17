from datetime import date, timedelta

from django.core.urlresolvers import resolve, reverse
from django.http import Http404
from django.test import RequestFactory, TestCase
from model_mommy import mommy

from .models import Iteration
from .views import DayEditionView, TodayEditionView


class EditionURLTests(TestCase):
    """
    Are the URLs calling the correct views?
    """

    def test_implicit_today_url(self):
        view = resolve('/edition/matt/')[0]
        self.assertEqual(view.__name__, 'TodayEditionView')

    def test_today_url(self):
        view = resolve('/edition/matt/today/')[0]
        self.assertEqual(view.__name__, 'TodayEditionView')

    def test_day_url(self):
        view = resolve('/edition/matt/2014/12/25/')[0]
        self.assertEqual(view.__name__, 'DayEditionView')

    def test_day_month_name_url(self):
        view = resolve('/edition/matt/2014/dec/25/')[0]
        self.assertEqual(view.__name__, 'DayEditionView')


class EditionContextTests(TestCase):
    """
    Do the views contain the correct context data?
    """

    def setUp(self):
        self.factory = RequestFactory()

        self.becia = mommy.make('auth.User')
        self.matt = mommy.make('auth.User')
        self.ewa = mommy.make('auth.User')

    def test_user_does_not_exist(self):
        """
        If the user does not exist, return a 404.
        """
        with self.assertRaises(Http404):
            username = 'JonSnow'

            url = reverse('edition_today', args=[username])
            request = self.factory.get(url)
            TodayEditionView.as_view()(request, user=username)

    def test_user_empty(self):
        """
        Iterations exist for other users, but not for `Ewa`. Return a 404 if
        the user has no iterations.
        """
        pearl = mommy.make('core.Pearl', user=self.becia)
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)

        pearl = mommy.make('core.Pearl', user=self.matt)
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)

        with self.assertRaises(Http404):
            username = self.ewa.username

            url = reverse('edition_today', args=[username])
            request = self.factory.get(url)
            TodayEditionView.as_view()(request, user=username)

    def test_user_limited_today(self):
        """
        Ability to limit iterations to a user and those which are active today.
        """
        user = self.matt
        username = self.matt.username

        pearl = mommy.make('core.Pearl', user=user)

        # Iterations for today. This `should` show.
        iterations = [
            mommy.make('core.Iteration', date=date.today(), pearl=pearl),
        ]

        # Iterations in the past and future. These should `not` show.
        mommy.make('core.Iteration', date=date.today()-timedelta(5), pearl=pearl)
        mommy.make('core.Iteration', date=date.today()+timedelta(5), pearl=pearl)

        url = reverse('edition_today', args=[username])
        request = self.factory.get(url)
        response = TodayEditionView.as_view()(request, user=username)

        self.assertEqual(
            list(response.context_data['iteration_list']),
            list(iterations),
        )

    def test_future_date(self):
        """
        Ability to limit iterations to a specified user and a date in the
        future.
        """
        user = self.matt
        username = self.matt.username
        future_date = date.today() + timedelta(5)

        pearl = mommy.make('core.Pearl', user=user)

        # Iteration on a future date. This `should` show.
        mommy.make('core.Iteration', date=future_date, pearl=pearl)

        # Iterations for today and in the past. These should `not` show.
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)
        mommy.make('core.Iteration', date=date.today()-timedelta(5), pearl=pearl)

        url = reverse('edition_day', args=[
            username,
            future_date.year,
            future_date.month,
            future_date.day,
        ])

        request = self.factory.get(url)

        response = DayEditionView.as_view(month_format='%m')(
            request,
            user=username,
            year=str(future_date.year),
            month=str(future_date.month),
            day=str(future_date.day),
        )

        self.assertEqual(
            list(response.context_data['iteration_list']),
            list(Iteration.objects.filter(date=future_date)),
        )

    def test_past_date(self):
        """
        Ability to limit iterations to a user and a date in the past.
        """
        user = self.matt
        username = self.matt.username
        past_date = date.today() - timedelta(5)

        pearl = mommy.make('core.Pearl', user=user)

        # Iteration on a past date. This `should` show.
        mommy.make('core.Iteration', date=past_date, pearl=pearl)

        # Iterations for today and in the future. These should `not` show.
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)
        mommy.make('core.Iteration', date=date.today()+timedelta(5), pearl=pearl)

        url = reverse('edition_day', args=[
            username,
            past_date.year,
            past_date.month,
            past_date.day,
        ])

        request = self.factory.get(url)

        response = DayEditionView.as_view(month_format='%m')(
            request,
            user=username,
            year=str(past_date.year),
            month=str(past_date.month),
            day=str(past_date.day),
        )

        self.assertEqual(
            list(response.context_data['iteration_list']),
            list(Iteration.objects.filter(date=past_date)),
        )

    def test_total_time(self):
        """
        Does the template context have the correct total time for iterations?
        """
        user = self.matt
        username = self.matt.username

        pearl = mommy.make('core.Pearl', minutes=3, user=user)
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)
        mommy.make('core.Iteration', date=date.today(), pearl=pearl)

        url = reverse('edition_today', args=[username])
        request = self.factory.get(url)
        response = TodayEditionView.as_view()(request, user=username)

        self.assertEqual(response.context_data['total_time'], '9 minutes')
