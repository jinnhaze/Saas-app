from rest_framework import serializers
from .models import *



class CreditBalanceSerializer(serializers.ModelSerializer):
    class Meta :
        models = CreditBalance
        fields = ["credits","last_updated"]



class UsageLogSerializer(serializers.ModelSerializer):
    class Meta :
        models = UsageLog
        fields = ["feature","prompt","credits_deducted","created_at"]        