from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from usage.models import UsageLog, CreditBalance
from subscriptions.models import UserSubscription



class DashboardView(APIView):
    def get(self,request):
        user = request.user
        
        
        try :
            credit_balance = CreditBalance.objects.get(user=user)
            credits = credit_balance.credits
            
        except CreditBalance.DoesNotExist :
            
            credits = 0
            
            
            
        try :
            subscription = UserSubscription.objects.get(user=user)
        
        except UserSubscription.DoesNotExist :
            subscription = None
            
            
            
        recent_usage = UsageLog.objects.filter(user=user).order_by("created_at")[:10]
        
        
        total_generations = UsageLog.objects.filter(user=user).count()
        
        
        
        data = {
            "credits" : credits,
            
            "subscription" : {
                "plan_name": subscription.plan.name if subscription else "Free",
                "status": subscription.status if subscription else "inactive",
                "current_period_end": subscription.current_period_end if subscription else None
            },
            "recent_usage": [
                {
                    "feature": log.feature,
                    "credits_deducted": log.credits_deducted,
                    "created_at": log.created_at
                } for log in recent_usage
            ],
            "total_generations": total_generations
        }
        
        return Response(data)
            
            
            
                    
                
            