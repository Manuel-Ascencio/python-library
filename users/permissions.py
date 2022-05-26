from rest_framework import permissions

class IsOwnwerOrReadOnly(permissions.BasePermission):
    
    def has_object_permissions(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_superuser or request.user.is_staff:
            return True

        return obj == request.user