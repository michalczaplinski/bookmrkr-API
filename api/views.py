from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse

from main.models import Bookmark, Tag
from api.serializers import BookmarkSerializer, TagSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def list(self, request, *args, **kwargs):
        queryset = Bookmark.objects.filter(owner=request.user)
        serializer = BookmarkSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        ''' This overrides the method in mixins.CreateModelMixin
            which is mixed into ModelViewSet
        '''
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)

    #
    # def destroy(self, request, *args, **kwargs):
    #     super(BookmarkViewSet, self).destroy(request, *args, **kwargs)

    # TODO add an update() method here.
    # http://www.django-rest-framework.org/api-guide/serializers/#writing-update-methods-for-nested-representations


class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request, *args, **kwargs):
        queryset = Tag.objects.filter(owner=request.user)
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        ''' This overrides the method in mixins.CreateModelMixin
            which is mixed into ModelViewSet
        '''
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


@ensure_csrf_cookie
def get_token(request):
    return HttpResponse("here's your CSRF token")
