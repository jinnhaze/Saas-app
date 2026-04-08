from rest_framework.response import Response
from .serializers import Registerserializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(APIView):
    def post(self,request):
           

           serializer = Registerserializer(data = request.data)


           if serializer.is_valid():

            serializer.save()

            return Response({'message':'user is created'})
           
           return Response(serializer.errors)   


class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        return Response({'error' : 'invalid credentials'})

   