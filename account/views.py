from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from account.models import User

from account.serializers import RegisterUserSerializer, LoginUserSerializer, UserSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@api_view(['POST'])
def registration_view(request):
    serializer = RegisterUserSerializer(data=request.data)

    if serializer.is_valid():
        new_user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_by_email(request):
    email = request.data['email']
    password = request.data['password']

    user = authenticate(email=email, password=password)

    if user is not None:
        login(request, user)
        return Response(status=status.HTTP_200_OK)

    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
