from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class CreditBalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        balance,created = CreditBalance.objects.get_or_create(user=request.user)
        serializers = CreditBalanceSerializer(balance)
        return Response(serializers.data)
    


class UsageLogView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        logs = UsageLog.objects.filter(user=request.user)
        serializers = UsageLogSerializer(logs,many=True)
        return Response(serializers.data)

