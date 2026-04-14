from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PlanView(APIView):
    def get(self,request):
        plan = SubscriptionPlan.objects.filter(is_active = True)
        serializer = SubscriptionPlanSerializer(plan,many=True)
        return Response(serializer.data)
    

class MySubscriptionView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):

        try :
            subscription = request.user.subscription
            serializer = UserSubscriptionSerializer(subscription)
            return Response(serializer.data)
        
        except UserSubscription.DoesNotExist :
            return Response({"serializerdetail": "No active subscription found"}, status=status.HTTP_404_NOT_FOUND)
        
        
        

class PaymentView(APIView):
            permission_classes = [IsAuthenticated]
            
            def post(self,request):
                plan_id = request.user.get("plan_id ")
                
                try :
                    plan = SubscriptionPlan.objects.get(id=plan_id,is_active = True)
                    
                    
                    payment = Payment.objects.create(
                        user = request.user,
                        plan = plan,
                        amount = plan.price,
                        status = "pending"
                    )
                    
                    serializer = PaymentSerializer(payment)
                    
                    return Response({
                "message": "Order created successfully",
                "payment": serializer.data
            })
                    
                    
                except SubscriptionPlan.DoesNotExist :
                    return Response({"error": "Plan not found"}, status=status.HTTP_400_BAD_REQUEST)    
                           
            
        
    

            