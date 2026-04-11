from rest_framework.exceptions import PermissionDenied
from .models import CreditBalance, UsageLog


def check_and_deduct_credits(user,feature:str,prompt:str="",credits_to_deduct:int=1):
    balance,_ = CreditBalance.objects.get_or_create(user=user)
    if balance.credits < credits_to_deduct:
        raise PermissionDenied("You don't have enough credits. Please purchase more")
    
    balance.credits -= credits_to_deduct
    balance.save()


    UsageLog.objects.create(
        user = user,
        feature = feature,
        prompt=prompt[:500],
        credits_deducted = credits_to_deduct
     
    )

    return True