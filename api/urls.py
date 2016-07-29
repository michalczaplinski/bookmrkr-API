from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from api.views import BookmarkViewSet, TagViewSet, BookmarkSearchView, get_token


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('bookmarks', BookmarkViewSet)
router.register('tags', TagViewSet)
router.register("search", BookmarkSearchView, base_name="bookmark-search")

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^get_token', get_token)
]