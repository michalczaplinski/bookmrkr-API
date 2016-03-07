import os.path
import os
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.renderers import JSONRenderer

from api.serializers import BookmarkSerializer
from .factories import TagFactory, BookmarkFactory
from django.conf import settings
from main.models import Bookmark, Tag

user = User.objects.get(username='test')


def _clean_up_uploads(self):
    # check if the instance of our Test Case has the attribute 'response'
    if hasattr(self, 'response') and 'cover' in self.response:
        # if it does, get the path to the uploaded file and if it exist, remove the file.
        uploaded_file_path = os.path.join(settings.MEDIA_ROOT, self.response.data['cover'].split('/')[-1])
        if os.path.isfile(uploaded_file_path):
            os.remove(uploaded_file_path)


class TestGets(APITestCase):

    def setUp(self):
        self.client.force_authenticate(user=user)

    def test_getting_the_api_root(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('bookmarks', response.data)
        self.assertIn('tags', response.data)

    def test_getting_bookmarks(self):
        response = self.client.get('/api/bookmarks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 0)

    def test_getting_tags(self):
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 0)


class TestCreate(APITestCase):

    def setUp(self):
        self.client.force_authenticate(user=user)
        self.upload_data = {
            "url": "http://test.bookmark1.com",
            "title": "test bookmark 1",
            "description": "test bookmark 1 description",
            "cover": None,
            "content": "",
            "date_created": "2016-02-20T17:55:20.126462Z",
            "date_updated": "2016-02-20T17:55:20.126487Z",
            "owner": "test",
            "tags": [],
            "is_trashed": "false",
            "domain": "bookmark1.com"
        }

    def tearDown(self):
        _clean_up_uploads(self)

    def test_create_a_bookmark_with_cover_photo(self):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_image.jpg')
        with open(image_path, 'rb') as cover_photo:
            self.upload_data['cover'] = cover_photo
            self.response = self.client.post('/api/bookmarks/', self.upload_data, format='multipart')
            self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)

            # test if the uploaded file exists
            self.assertTrue(os.path.isfile(os.path.join(settings.MEDIA_ROOT, self.response.data['cover'].split('/')[-1])))

    def test_create_bookmark_with_a_tag(self):
        tag_name = 'test tag 1'
        self.upload_data['tags'] = [{"name": tag_name}]
        self.response = self.client.post('/api/bookmarks/', self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Bookmark.objects.filter(url='http://test.bookmark1.com').exists())
        self.assertTrue(Tag.objects.filter(name=tag_name).exists())

    def test_create_bookmark_with_2_tags(self):
        tag_data = [{"name": "test tag 1"}, {"name": "test tag 2"}]
        self.upload_data['tags'] = tag_data
        self.response = self.client.post('/api/bookmarks/', self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Bookmark.objects.filter(url='http://test.bookmark1.com').exists())

        tags = Bookmark.objects.get(url="http://test.bookmark1.com").tags.all().iterator()
        for index, tag in enumerate(tags):
            self.assertEqual(tag.name, tag_data[index]['name'])

    def test_create_bookmark_with_already_existing_tag(self):
        tag = TagFactory.create()
        BookmarkFactory.create(tags=(tag,))

        self.upload_data['tags'] = [{"name": 'Very Fun', "color": '#00BCD4'}]
        self.response = self.client.post('/api/bookmarks/', self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Bookmark.objects.filter(url='http://test.bookmark1.com').exists())
        self.assertTrue(Bookmark.objects.filter(tags__name='Very Fun').exists())


class TestUpdate(APITestCase):

    def setUp(self):
        self.client.force_authenticate(user=user)
        self.bookmark = BookmarkFactory.create()
        self.url = '/api/bookmarks/{id:d}/'.format(id=self.bookmark.id)
        self.upload_data = BookmarkSerializer(self.bookmark).data

    def tearDown(self):
        _clean_up_uploads(self)

    def test_updating_bookmark_title(self):
        self.upload_data['title'] = 'NEW TEST TITLE'
        self.response = self.client.put(self.url, self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_200_OK)
        self.assertTrue(Bookmark.objects.filter(title='NEW TEST TITLE').exists())

    def test_updating_bookmark_title_and_url(self):
        self.upload_data['title'] = 'NEW TEST TITLE'
        self.upload_data['url'] = 'http://www.new.url.com'

        self.response = self.client.put(self.url, self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_200_OK)
        self.assertTrue(Bookmark.objects.filter(title='NEW TEST TITLE').exists())
        self.assertTrue(Bookmark.objects.filter(url='http://www.new.url.com').exists())

    def test_updating_bookmark_tag(self):
        self.upload_data['tags'] = [{'name': 'NEW TAG'}]

        self.response = self.client.put(self.url, self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_200_OK)
        self.assertTrue(Bookmark.objects.filter(tags__name='NEW TAG').exists())

    def test_updating_bookmark_tag_and_adding_a_new_one(self):
        tag1, tag2 = TagFactory.create_batch(size=2)
        self.bookmark = BookmarkFactory.create(tags=(tag1, tag2))

        self.url = '/api/bookmarks/{id:d}/'.format(id=self.bookmark.id)
        self.upload_data = BookmarkSerializer(self.bookmark).data
        self.upload_data['tags'] = [{'id': tag1.id, 'name': tag1.name, 'owner': 'test'},
                                    {'id': tag2.id, 'name': 'NEW TAG NAME', 'owner': 'test'}]

        self.response = self.client.put(self.url, self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_200_OK)
        self.assertTrue(Bookmark.objects.filter(tags__name=tag1.name, url=self.bookmark.url).exists())
        self.assertTrue(Bookmark.objects.filter(tags__name='NEW TAG NAME', url=self.bookmark.url).exists())
        self.assertFalse(Bookmark.objects.filter(tags__name=tag2.name, url=self.bookmark.url).exists())

    def test_updating_bookmark_tag_and_deleting_one(self):
        tag1, tag2 = TagFactory.create_batch(size=2)
        self.bookmark = BookmarkFactory.create(tags=(tag1, tag2))

        self.url = '/api/bookmarks/{id:d}/'.format(id=self.bookmark.id)
        self.upload_data = BookmarkSerializer(self.bookmark).data
        self.upload_data['tags'] = [{'id': tag2.id, 'name': 'NEW TAG NAME', 'owner': 'test'}]

        self.response = self.client.put(self.url, self.upload_data)

        self.assertEquals(self.response.status_code, status.HTTP_200_OK)

        # the first bookmark does not exist
        self.assertFalse(Bookmark.objects.filter(tags__name=tag1.name, url=self.bookmark.url).exists())
        # self.assertFalse(Tag.objects.filter(name=tag1.name).exists())

        # the updated tag exists
        self.assertTrue(Bookmark.objects.filter(tags__name='NEW TAG NAME', url=self.bookmark.url).exists())

        # the tag with the old name does not exist
        self.assertFalse(Bookmark.objects.filter(tags__name=tag2.name, url=self.bookmark.url).exists())
        # self.assertFalse(Tag.objects.filter(name=tag2.name).exists())


class TestDeletes(APITestCase):

    def setUp(self):
        self.client.force_authenticate(user=user)

    def test_deleting_a_bookmark(self):
        tag1, tag2 = TagFactory.create_batch(size=2)
        self.bookmark1 = BookmarkFactory.create(tags=(tag1,tag2))
        self.bookmark2 = BookmarkFactory.create()

        self.url = '/api/bookmarks/{id:d}/'.format(id=self.bookmark1.id)

        self.response = self.client.delete(self.url)

        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Bookmark.objects.filter(id=self.bookmark1.id).exists())
        self.assertTrue(Bookmark.objects.filter(id=self.bookmark2.id).exists())


    #TODO: test that disallowed methods are truly disallowed:
    #       - e.g. you cannot create Tags directly, only through creation of a Bookmark