from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Bookmark, Tag
from api.serializers import BookmarkSerializer, TagSerializer

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
        ''' This overrides the method in mixins.CreateModelMixin
            which is mixed into ModelViewSet
        '''
        serializer.save(owner=self.request.user)

    # TODO add an update() method here.
    # http://www.django-rest-framework.org/api-guide/serializers/#writing-update-methods-for-nested-representations


    # don't think that explict csrf exemption is necessary here.
    # @method_decorator(csrf_exempt)
    # def dispatch(self, *args, **kwargs):
    #     return super(BookmarkViewSet, self).dispatch(*args, **kwargs)


class TagViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        queryset = Tag.objects.filter(owner=request.user)
        serializer = TagSerializer
        return Response(serializer.data)


