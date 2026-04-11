from django.db import models
from django.conf import settings
from django.utils import timezone


class CreditBalance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="credit_balance")
    credits = models.PositiveIntegerField(default=25)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.credits}credits"
    


class UsageLog(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="usage_log")
    feature = models.CharField(max_length=50)
    prompt = models.TextField(null=True,blank=True)
    tokens_used = models.PositiveIntegerField(default=0)
    credits_deducted = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta :
        ordering = ["-created_at"]


    def __str__(self):
        return f"{self.user.email} - {self.feature} - {self.credits_deducted}credits"    

