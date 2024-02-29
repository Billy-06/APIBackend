from rest_framework import permissions

class ProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow POST, PUT, PATCH, DELETE requests only for authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow PUT, PATCH, DELETE requests only if the user is the owner of the project
        return obj.user == request.user


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow POST request only for authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests only if the user is the owner of the user object
        return obj == request.user


class ArticlePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow POST request only for authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, OPTIONS requests for all users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow PUT, PATCH, DELETE requests only if the user is the author of the article
        return obj.author == request.user
