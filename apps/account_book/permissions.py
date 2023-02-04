from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_authenticated:
            if user.is_admin:
                return True
            elif obj.__class__ == get_user_model():
                return obj.id == user.id
            elif hasattr(obj, "user"):
                return obj.user.id == user.id
            elif hasattr(obj, "account_book"):
                return obj.account_book.user.id == user.id
            return False
        return False
