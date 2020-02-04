from django.db import models


class Contractor(models.Model):
    created = models.DateTimeField()
    updated = models.DateTimeField()
    name = models.CharField()
    skills = models.ExpressionList()
    email = models.EmailField()
    phone_number = models.CharField()
    cv = models.CharField()
    # VAT number
    # company name


class Client(models.Model):
    pass
