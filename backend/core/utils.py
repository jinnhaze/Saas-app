from usage.models import CreditBalance,UsageLog


def get_user_credits(user):
    
    try :
        return CreditBalance.objects.get(user=user).credits
    
    except CreditBalance.DoesNotExist:
        return 0
    
    
    
    
def has_enough_credits(user,amount=1,feature = "unknown"):
    
    try :
        balance = CreditBalance.objects.get(user=user)
        
        if balance.credits >= amount :
            balance.credits -= amount
            balance.save()
            
            
            
            UsageLog.objects.create(
                user = user,
                feature = feature,
                credits_deducted = amount
            )
            
            return True
        
        return False
    
    except CreditBalance.DoesNotExist :
        return False
        