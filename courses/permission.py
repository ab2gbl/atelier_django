
from rest_framework import permissions
from .models import Path_Instructor,Branche,Path
from rest_framework.permissions import BasePermission, IsAdminUser


class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role=="INSTRUCTOR")  

class IsInPath(permissions.BasePermission):
    def has_permission(self, request, view):
        branche_id = request.data.get('branche_id')
        try:
            branche = Branche.objects.get(id=branche_id)
            path = branche.path
            return bool(request.user and request.user.role == "INSTRUCTOR" and Path_Instructor.objects.filter(path=path, instructor=request.user).exists())
        except Branche.DoesNotExist:
            return False
        
class IsAuthorOrChefOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        chef=obj.branche.path.chef
        return user.is_authenticated and (obj.instructor == user or user==chef or IsAdminUser().has_permission(request, view))

class IsChefOrAdminCreate(BasePermission):
    def has_permission(self, request, view):
        
        user = request.user
        # Check if the user is an admin
        if IsAdminUser().has_permission(request, view ):
            return True
        path_name = request.data.get('path_name')  # Note: You might need to handle 'path' differently
        if path_name is None:
            return False
        
        try:
            path = Path.objects.get(name=path_name)
            chef = path.chef
            return user.is_authenticated and user == chef
        except Path.DoesNotExist:
            return False
        
class IsChefOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        chef=obj.path.chef
        return user.is_authenticated and (user==chef or IsAdminUser().has_permission(request, view))
