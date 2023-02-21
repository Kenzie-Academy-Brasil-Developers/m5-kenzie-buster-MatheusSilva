
from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User

class CustomPermission(permissions.BasePermission):

    def has_permission(self, req: Request, view: View ):

        if req.method in permissions.SAFE_METHODS:
            return True

        if req.user.is_authenticated and req.user.is_employee:
            return True

        return False

class CustomIsAuthenticated(permissions.BasePermission):

    def has_object_permission(self, req: Request, view: View, user: User):

        if req.user.is_authenticated and req.user.is_superuser:
            return True

        if req.user and req.user.is_authenticated and user.id == req.user.id:

            return True
        
        return False