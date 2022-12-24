from rest_framework import permissions

class IsUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return bool(obj.pk == request.user.pk)
        return bool(obj.pk == request.user.pk)