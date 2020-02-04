from django.db import models

from accounts.models import Contractor, Client


class Project(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    duration = models.IntegerField()
    # below: choices: week, month, days, years
    duration_term = models.CharField()
    poster = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    # for now the below is just the daily rate
    budget = models.FloatField()
    # let's see about the below, you can always create a new table with this
    # and make foreign keys
    skills = models.ExpressionList()


class Applications(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    deleted = models.DateTimeField()
    candidate = models.ForeignKey(to=Contractor, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Client, on_delete=models.CASCADE)
