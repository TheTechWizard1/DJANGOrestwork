from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserAuthSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def authorization_api_view(request):
    #Validation
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    #Authentication
    user = authenticate(**serializer.validated_data)
    if user:
        try:
            token = Token.objects.get(user=user)
        except:
            token = Token.objects.get(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'User credentials are wrong!'})



@api_view(['POST'])
def registration_api_view(request):
    #Validation
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    #Create user
    user = User.objects.create_user(**serializer.validated_data)

    #Return Response
    return Response(status=status.HTTP_201_CREATED,
                    data={'user_id': user.id})