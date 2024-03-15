from rest_framework import permissions, exceptions


class ClientAccessPermission(permissions.BasePermission):
    """
    Класс разрешений для доступа к записям клиентов.
    Проверяет, что пользователь аутентифицирован для просмотра записей.
    Также проверяет, что пользователь является автором записи
    или администратором для выполнения изменений или удаления записей.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if not (request.user == obj.user or request.user.is_staff):
            raise exceptions.PermissionDenied(
                "Вы являетесь не автором данной записи, обратитесь к администратору"
            )
        return True
