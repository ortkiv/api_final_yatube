from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Кастомный пермишен.

    Разрешает не безопасные методы
    (POST, PUT, PATCH, DELETE)
    только для автора обьекта.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
