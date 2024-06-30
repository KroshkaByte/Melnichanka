from rest_framework import permissions, exceptions


class ClientAccessPermission(permissions.BasePermission):
    """
    Permission class for accessing client records.

    Checks that the user is authenticated to view records.
    Additionally, verifies that the user is either the author of the record
    or an administrator to perform changes or deletions on records.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if not (request.user == obj.user or request.user.is_staff):
            raise exceptions.PermissionDenied(
                "Вы являетесь не автором данной записи, обратитесь к администратору"
            )
        return True
