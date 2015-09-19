from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt


from api.views import BookmarkViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', csrf_exempt(include('rest_auth.urls')))
]
