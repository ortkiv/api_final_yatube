from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Кастомный пермишен.

    Разрешает изменение и удаление обьекта
    только его автору.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
