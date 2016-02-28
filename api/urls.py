from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter


from api.views import BookmarkViewSet, TagViewSet, get_token

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register('bookmarks', BookmarkViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^get_token', get_token)
]
