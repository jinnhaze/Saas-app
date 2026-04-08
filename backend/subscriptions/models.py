from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()



class Plan(models.Model):

    PLAN_CHOICES = (
        ('free', 'Free'),
        ('pro', 'Pro'),
    )

    name = models.CharField(max_length=20, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    duration_days = models.PositiveIntegerField(help_text="Duration in days")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    is_active = models.BooleanField(default=True)

    # Payment (optional but important for real apps)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    payment_status = models.CharField(max_length=20, default='pending')  # pending, paid, failed

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Auto calculate end_date
        if self.start_date and self.plan:
            self.end_date = self.start_date + timedelta(days=self.plan.duration_days)

        # Auto update status
        if self.end_date and timezone.now() > self.end_date:
            self.status = 'expired'
            self.is_active = False

        super().save(*args, **kwargs)

    def is_expired(self):
        return self.end_date and timezone.now() > self.end_date

    def __str__(self):
        return f"{self.user} - {self.plan} ({self.status})"



class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user} current plan"