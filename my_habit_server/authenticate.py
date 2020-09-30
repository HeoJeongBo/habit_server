import jwt
from django.conf import settings
from rest_framework import authentication
from account.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(
                jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            id = decoded.get("id")
            user = User.objects.get(id=id)
            return (user, None)
        except (ValueError, jwt.exceptions.DecodeError, User.DoesNotExist):
            return None
