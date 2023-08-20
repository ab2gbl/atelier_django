
from rest_framework import permissions
from .models import Path_Instructor,Branche

    
class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role=="INSTRUCTOR")  

class IsInPath(permissions.BasePermission):
    def has_permission(self, request, view):
        branche_id = request.data.get('branche')
        try:
            branche = Branche.objects.get(id=branche_id)
            path = branche.path
            return bool(request.user and request.user.role == "INSTRUCTOR" and Path_Instructor.objects.filter(path=path, user=request.user).exists())
        except Branche.DoesNotExist:
            return False