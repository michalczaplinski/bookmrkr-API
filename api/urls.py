from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api.views import BookmarkViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
