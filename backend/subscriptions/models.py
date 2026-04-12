from django.db import models
from django.conf import settings
from django.utils import timezone



class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    credits_per_month = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name} - ₹{self.price}/month"
    



class UserSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="subscription")
    plan = models.ForeignKey(SubscriptionPlan,on_delete=models.PROTECT)
    razropay_subscription_id = models.CharField(max_length=100,blank=True,null=True)
    status = models.CharField(max_length=20,default="active")
    current_period_end = models.DateTimeField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.email} - {self.plan.name}"
    


class Payment(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
     plan = models.ForeignKey(SubscriptionPlan,on_delete=models.PROTECT)
     razropay_order_id = models.CharField(max_length=100)
     razropay_payment_id = models.CharField(max_length=100,blank=True,null=True)
     amount = models.DecimalField(max_digits=10,decimal_places=2)
     status = models.CharField(max_length=20,default="pending")
     created_at = models.DateTimeField(auto_now_add=True)


     def __str__(self):
         return f"{self.user.email} - {self.amount} - {self.status}"


