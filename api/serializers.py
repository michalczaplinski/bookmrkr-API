from rest_framework import serializers
from main.models import Bookmark, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class BookmarkSerializer(serializers.ModelSerializer):

    # not sure if owner and cover are needed
    owner = serializers.ReadOnlyField(source='owner.username')
    cover = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False, use_url=True)
    tags = TagSerializer(required=False, many=True)

    class Meta:
        model = Bookmark
        fields = ('id',
                  'url',
                  'title',
                  'description',
                  'content',
                  'cover',
                  'date_created',
                  'date_updated',
                  'owner',
                  'tags',
                  'is_trashed',
                  'domain')

    def create(self, validated_data):
        tags = validated_data['tags']
        validated_data.pop('tags')

        bookmark = Bookmark.objects.create(**validated_data)
        for tag in tags:
            print(tag)
            t = Tag.objects.create(**tag)
            bookmark.tags.add(t)
        return bookmark

    # TODO:
    # update
    # delete