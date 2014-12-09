from django.core.urlresolvers import resolve
from django.test import TestCase


class EditionURLTests(TestCase):
    """
    Are the URLs calling the correct views?
    """

    def test_implicit_today_url(self):
        response = self.client.get('/edition/matt/')
        view = resolve(response.request['PATH_INFO'])[0]
        self.assertEqual(view.__name__, 'TodayEditionView')

    def test_today_url(self):
        response = self.client.get('/edition/matt/today/')
        view = resolve(response.request['PATH_INFO'])[0]
        self.assertEqual(view.__name__, 'TodayEditionView')

    def test_day_url(self):
        response = self.client.get('/edition/matt/2014/12/25/')
        view = resolve(response.request['PATH_INFO'])[0]
        self.assertEqual(view.__name__, 'DayEditionView')

    def test_day_month_name_url(self):
        response = self.client.get('/edition/matt/2014/dec/25/')
        view = resolve(response.request['PATH_INFO'])[0]
        self.assertEqual(view.__name__, 'DayEditionView')
