from rest_framework import serializers
from usage.models import CreditBalance,UsageLog
from subscriptions.models import SubscriptionPlan,UserSubscription
from ai_engine.models import AIGeneration


class CreditBalanceSerializer(serializers.ModelSerializer):
    class Meta :
        model = CreditBalance
        fields = ["credits","last_updated"]
        
        
        
class UsageLogSerializer(serializers.ModelSerializer):
    class Meta :
        model = UsageLog
        fields = ['id', 'feature', 'prompt', 'credits_deducted', 'created_at']   
        
        
        
        
class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserSubscription     
        fields = ['plan', 'status', 'current_period_end']   
        
        
        
class DashboardSerializer(serializers.Serializer):
    credits = serializers.IntegerField()
    subscription = UserSubscriptionSerializer()
    recent_usage = UsageLogSerializer(many = True)
    total_generations = serializers.IntegerField()             