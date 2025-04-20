from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsMembers(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.members.filter(user=request.user).exists()  # exist bormi digan narsa
