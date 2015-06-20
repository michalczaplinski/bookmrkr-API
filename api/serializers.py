from rest_framework import serializers
from main.models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id',
                  'url',
                  'title',
                  'cover',
                  'description',
                  'content',
                  # 'date_created',
                  # 'date_updated',
                  # 'owner',
                  'tags',
                  'is_trashed',
                  'domain')
