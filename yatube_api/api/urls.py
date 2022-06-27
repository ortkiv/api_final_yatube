from django.urls import include, path
from rest_framework import routers

from .views import (
    CommentViewsSet, FollowViewSet,
    GroupViewSet, PostViewSet, UserViewSet
)

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet)
router_v1.register(r'v1/groups', GroupViewSet)
router_v1.register(r'v1/follow', FollowViewSet, basename='follows')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewsSet, basename='comments'
)
router_v1.register(r'v1/users', UserViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
