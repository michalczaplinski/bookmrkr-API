from rest_framework import serializers
from main.models import Bookmark, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag


class BookmarkSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Bookmark
        fields = ('id',
                  'url',
                  'title',
                  'cover',
                  'description',
                  'content',
                  'date_created',
                  'date_updated',
                  'owner',
                  'tags',
                  'is_trashed',
                  'domain')

    def create(self, validated_data):
        tags = validated_data['tags']
        tt = []
        for tag in tags:
            print(tag)
            t = Tag.objects.create(**tag)
            tt.append(t)
        validated_data.pop('tags')
        Bookmark.objects.create(tags=tt, **validated_data)


