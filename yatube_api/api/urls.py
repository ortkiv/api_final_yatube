from django.urls import include, path
from rest_framework import routers

from .views import (CommentViewsSet, FollowCreateListRetrieveViewSet,
                    GroupViewSet, PostViewSet, UserViewSet)

router_v1 = routers.DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet, basename='posts')
router_v1.register(r'v1/groups', GroupViewSet, basename='groups')
router_v1.register(
    r'v1/follow',
    FollowCreateListRetrieveViewSet,
    basename='follows'
)
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewsSet, basename='comments'
)
router_v1.register(r'v1/customers', UserViewSet, basename='customers')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),

]
