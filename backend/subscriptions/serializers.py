from rest_framework import serializers
from .models import *


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = ['id', 'name', 'price', 'credits_per_month', 'description', 'is_active']


class UserSubscriptionSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source = "plan_name",read_only = True)
    class Meta :
        model = UserSubscription
        fields = ['id', 'plan', 'plan_name', 'status', 'current_period_end', 'created_at']    



class PaymentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Payment
        fields = ['id', 'plan', 'amount', 'status', 'created_at']           