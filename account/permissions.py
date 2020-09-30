from rest_framework.permissions import BasePermission


class IsSelf(BasePermission):
    def get_object_permission(self, request, view, user):
        return user == request.user
