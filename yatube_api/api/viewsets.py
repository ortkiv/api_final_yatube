from rest_framework import mixins, viewsets


class CreateListRetrieveViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """Вьюсет прокладка для сокращения строк
    и оптимизации в основной ветке."""
    pass
