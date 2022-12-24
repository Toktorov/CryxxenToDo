from rest_framework import permissions

class IsUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.pk == request.user.pk)