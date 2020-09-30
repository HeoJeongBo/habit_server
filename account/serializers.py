from rest_framework import serializers
from account.models import User
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'full_name',
            'password',
            'is_staff',
            'is_admin',
            'is_active'
        )
        # read_only_fields = ('')


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'full_name']

    def validate(self, data):
        email = data.get('email', None)
        full_name = data.get('full_name', None)
        password = data.get('password', None)

        if email is None or full_name is None or password is None:
            raise serializers.ValidationError(
                "email, full_name, password 같이 입력해주세요")
        return data

    def create(self):
        request_data = self.validated_data
        email = request_data.get('email', None)
        full_name = request_data.get('full_name', None)
        password = request_data.get('password', None)
        if email is None or full_name is None or password is None:
            serializers.ValidationError("email, password, full_name 모두 입력해주세요")
        new_user = User(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
        )
        password = self.validated_data['password']

        new_user.set_password(password)
        new_user.save()
        return new_user
