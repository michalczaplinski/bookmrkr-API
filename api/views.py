from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Bookmark, Tag
from api.serializers import BookmarkSerializer

class BookmarkViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def list(self, request):
        queryset = Bookmark.objects.filter(owner=request.user)
        serializer = BookmarkSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(BookmarkViewSet, self).dispatch(*args, **kwargs)