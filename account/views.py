from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from account.models import User

from account.serializers import RegisterUserSerializer, UserSerializer

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.decorators import action


class UserViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['POST'])
    def registration(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def login_by_email(self, request):
        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email)
        except:
            return Response({'message': '유저가 존재하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)

        if user is not None:
            responseSerializer = UserSerializer(user)
            userAuth = authenticate(email=email, password=password)
            if userAuth is not None:
                login(request, user)
                userSerializer = UserSerializer(user)
                return Response(userSerializer.data, status=status.HTTP_200_OK)
            return Response({'message': '비밀번호가 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)
