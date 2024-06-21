from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer
from .token import get_user_token


class UserRegisterAPIView(APIView):
    
    permission_classes = []

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    
    permission_classes = [] 
    
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            return Response({'error': "Email and Passoword required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)
        if user is None:
            return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': "User is not active"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserRegisterSerializer(user)
        token = get_user_token(user)
        return Response({'user': serializer.data,
                         'token': token,
                         },
                        status=status.HTTP_201_CREATED)
