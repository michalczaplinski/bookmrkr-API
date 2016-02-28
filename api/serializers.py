from rest_framework import serializers
from main.models import Bookmark, Tag
import datetime


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, source='owner.username', default=serializers.CurrentUserDefault())
    name = serializers.CharField(max_length=25)

    class Meta:
        model = Tag
        fields = ('id', 'name', 'owner')


class BookmarkSerializer(serializers.ModelSerializer):
    # not sure if owner and cover are needed
    owner = serializers.PrimaryKeyRelatedField(read_only=True, source='owner.username', default=serializers.CurrentUserDefault())
    cover = serializers.ImageField(allow_null=True, allow_empty_file=True, required=False,
                                   use_url=True)
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
        # tags = validated_data['tags']
        tags = validated_data.pop('tags')

        bookmark = Bookmark.objects.create(**validated_data)
        for tag in tags:
            new_tag = Tag.objects.get_or_create(name=tag.get('name'), owner=validated_data['owner'])
            bookmark.tags.add(new_tag[0])
        return bookmark

    def update(self, instance, validated_data):

        tags = validated_data.pop('tags')

        instance.url = validated_data.get('url', instance.url)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.content = validated_data.get('content', instance.content)
        # date created must stay unchanged
        # instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_updated = datetime.datetime.now()
        instance.type = validated_data.get('type', instance.type)
        instance.is_trashed = validated_data.get('is_trashed', instance.is_trashed)
        instance.domain = validated_data.get('domain', instance.domain)

        for tag in tags:
            # Returns a tuple of (object, created), where object is the retrieved or created object
            # and created is a boolean specifying whether a new object was created.
            new_tag, created = Tag.objects.get_or_create(name=tag.get('name'), owner=validated_data['owner'])
            if created:
                instance.tags.add(new_tag)
            else:
                # perhaps this is not needed
                instance.tags.update(new_tag)

        instance.cover = validated_data.get('cover', instance.cover)
        instance.save()
        return instance
