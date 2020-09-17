from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name']

    def save(self):
        new_user = User(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
        )
        password = self.validated_data['password']

        new_user.set_password(password)
        new_user.save()
        return new_user


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
