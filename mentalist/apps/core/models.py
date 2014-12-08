from django.db import models


class LittlePrinter(models.Model):
    """
    A physical Little Printer.
    """
    pass


class Pearl(models.Model):
    """
    A piece of information which when acted on over several iterations will
    result in the user memorising something. The piece of information itself
    does not have to be the thing being memorised, it could be a trigger or
    anything that causes concious effort to be applied to the information.

    This entity could be any of the following:

        + Question
        + Task
        + Fact
        + Definition
        + Image
    """
    pass


class Iteration(models.Model):
    """
    An iteration of an instance of a `Pearl`. There are six of these for every
    instance.
    """
    pass


class Delivery(models.Model):
    """
    An actual delivery that is sent to a specific Little Printer.
    """
    pass
