from rest_framework.permissions import BasePermission


class IsOwnerOrPostOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return request.user.is_authenticated
        return request.user.is_authenticated and obj.user.id == request.user.id


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.user.id == request.user.id
