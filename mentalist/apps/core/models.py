import requests
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from requests_oauthlib import OAuth1Session


class OAuth(models.Model):
    """
    Client and token credentials for 2-Legged OAuth 1.0 request.
    """
    name = models.CharField(max_length=50)
    client_key = models.CharField(max_length=50)
    client_secret = models.CharField(max_length=50)
    resource_owner_key = models.CharField(max_length=50)
    resource_owner_secret = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'OAuths'

    def __str__(self):
        return self.name


class LittlePrinter(models.Model):
    """
    A physical Little Printer.
    """
    name = models.CharField(max_length=50)
    subscription_id = models.CharField(max_length=50)
    credentials = models.ForeignKey('OAuth')

    def __str__(self):
        return self.name

    def print_edition(self, html):
        """
        Takes a string `html` and sends it to the Little Printer to be printed.
        """
        base_url = 'http://api.bergcloud.com/v1/subscriptions/{}/publish'

        berg = OAuth1Session(
            client_key=self.credentials.client_key,
            client_secret=self.credentials.client_secret,
            resource_owner_key=self.credentials.resource_owner_key,
            resource_owner_secret=self.credentials.resource_owner_secret,
        )

        berg.post(
            base_url.format(self.subscription_id),
            html,
            headers={'Content-Type': 'text/html; charset=utf-8'},
        )

    def test_print(self):
        """
        Sends a test page to the Little Printer.
        """
        self.print_edition('<h1>Test print from the Mentalist project!</h1>')

    def print_days_iteration(self, user, date):
        """
        Takes a `user` instance and a date then prints the user's iterations
        for that day. The reason this goes via the entire stack is to avoid
        repeating code, and to keep things separate.
        """
        url = reverse('edition_day', args=[
            user.username, date.year, date.month, date.day,
        ])

        base_url = getattr(settings, 'BASE_URL')

        response = requests.get(base_url + url)

        self.print_edition(response.content.decode())


class Pearl(models.Model):
    """
    A piece of information which when acted on over several iterations will
    result in the user memorising something. The piece of information itself
    does not have to be the thing being memorised, it could be a trigger or
    anything that causes concious effort to be applied to the information.

    This entity could be any of the following in nature:

        + Question
        + Task
        + Fact
        + Definition
        + Image
    """
    STATUS = Choices(
        ('question', _('question')),
        ('task', _('task')),
        ('fact', _('fact')),
        ('definition', _('definition')),
        ('image', _('image')),
    )

    status = models.CharField(choices=STATUS, default=STATUS.question, max_length=20)
    text = models.CharField(max_length=500, blank=True)
    answer = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    minutes = models.IntegerField(default=1)

    def __str__(self):
        return self.text[:35] + (self.text[35:] and '…')


class Iteration(models.Model):
    """
    An iteration of an instance of a `Pearl`. There are six of these for every
    instance.
    """
    user = models.ForeignKey('auth.User')
    pearl = models.ForeignKey('Pearl')
    date = models.DateField()
    iteration = models.IntegerField()

    def __str__(self):
        return '{}, {}, #{}: {}'.format(
            self.user,
            self.date,
            self.iteration,
            self.pearl,
        )
