
from rest_framework import permissions


    
class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user and request.user.role=="INSTRUCTOR")  
        else :
            return False

class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user and request.user.role=="COMPANY")  
        else :
            return False