import datetime
from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory, ImageField
from main.models import Bookmark, Tag


class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = 'Very Fun'
    color = '#00BCD4'
    owner = User.objects.get(username='test')


class BookmarkFactory(DjangoModelFactory):
    class Meta:
        model = Bookmark

    url = 'http://example.com'
    title = 'Fun website'
    cover = None
    description = 'Lorem ipsum'
    content = 'lorem ipsum'
    date_created = datetime.datetime.now()
    date_updated = datetime.datetime.now()
    owner = User.objects.get(username='test')
    type = 'Link'
    is_trashed = False
    domain = 'example.com'

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of tags were passed in, use them
            for tag in extracted:
                self.tags.add(tag)