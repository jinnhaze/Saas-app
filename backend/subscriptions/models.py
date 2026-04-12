from django.db import models
from django.conf import settings
from django.utils import timezone



class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    credits_per_month = 