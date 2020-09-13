from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from account.serializers import RegisterUserSerializer

# Create your views here.


@api_view(['POST'])
def registration_view(request):
    serializer = RegisterUserSerializer(data=request.data)

    if serializer.is_valid():
        new_user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
