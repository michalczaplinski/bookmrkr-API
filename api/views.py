from django.contrib.auth.models import User

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
        # tags = serializer.data['tags']

        # print(tags)

        # if serializer.is_valid():
        #     for tag in tags:
        #         print(tag)
        #         t = Tag(name=tag)
        #         t.save()

        # else:
        #     return Response({'data': serializer.errors})

        serializer.save(owner=self.request.user)

