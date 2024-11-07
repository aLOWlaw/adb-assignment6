from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'seller' or request.user.is_admin:
            return True
