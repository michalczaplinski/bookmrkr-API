from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from main.models import Bookmark
from api.serializers import BookmarkSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
