
from rest_framework import permissions

from rest_framework.permissions import BasePermission, IsAdminUser



class IsDeveloper(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and bool(request.user and request.user.role=="DEVELOPER")  
