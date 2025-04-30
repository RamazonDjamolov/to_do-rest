from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsownerIntaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user == obj.project.owner, "Is owner")
        return request.user == obj.project.owner

class IsmemberTaskPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        x = obj.project

        return  x.members.filter(user=request.user).exists()

        # return obj.project.members.filter(user=request.user).exists()
from rest_framework.permissions import BasePermission

class IsMemberOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            IsmemberTaskPermission().has_object_permission(request, view, obj) or
            IsownerIntaskPermission().has_object_permission(request, view, obj)
        )




class IsMembers(BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.members.filter(user=request.user).exists()  # exist bormi digan narsa
