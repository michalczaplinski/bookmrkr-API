import os.path
import os
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .factories import TagFactory, BookmarkFactory
from django.conf import settings
from main.models import Bookmark, Tag

user = User.objects.get(username='test')


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

        # check if the instance of our Test Case has the attribute 'response'
        if hasattr(self, 'response') and 'cover' in self.response:
            # if it does, get the path to the uploaded file and if it exist, remove the file.
            uploaded_file_path = os.path.join(settings.MEDIA_ROOT, self.response.data['cover'].split('/')[-1])
            if os.path.isfile(uploaded_file_path):
                os.remove(uploaded_file_path)

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
        self.response = self.client.post('/api/bookmarks/', self.upload_data, format='json')

        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Bookmark.objects.filter(url='http://test.bookmark1.com').exists())
        self.assertTrue(Tag.objects.filter(name=tag_name).exists())

    def test_create_bookmark_with_2_tags(self):
        tag_data = [{"name": "test tag 1"}, {"name": "test tag 2"}]
        self.upload_data['tags'] = tag_data
        self.response = self.client.post('/api/bookmarks/', self.upload_data, format='json')

        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Bookmark.objects.filter(url='http://test.bookmark1.com').exists())

        tags = Bookmark.objects.get(url="http://test.bookmark1.com").tags.all().iterator()
        for index, tag in enumerate(tags):
            self.assertEqual(tag.name, tag_data[index]['name'])

    def test_create_bookmark_with_already_existing_tag(self):
        tag = TagFactory.create()
        bookmark = BookmarkFactory.create(tags=(tag,))

        self.upload_data['tags'] = [{"name": 'Very Fun', "color": '#00BCD4'}]
        self.response = self.client.post('/api/bookmarks/', self.upload_data, format='json')

        self.assertEquals(self.response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Bookmark.objects.filter(url='http://test.bookmark1.com').exists())
        self.assertTrue(Bookmark.objects.filter(tags__name='Very Fun').exists())


class TestUpdate(APITestCase):

    def setUp(self):
        self.client.force_authenticate(user=user)
        self.bookmark = BookmarkFactory.build()

    def test_updating_bookmark_title(self):
        pass

    def test_updating_bookmark_title_and_url(self):
        pass

    def test_updating_bookmark_tag(self):
        pass


class TestComplexUpdates(APITestCase):
    """
    Tests which use existing data.
    """

    def setUp(self):
        self.client.force_authenticate(user=user)
        self.bookmark = BookmarkFactory.build()

    def test_updating_bookmark_tag_and_adding_a_new_one(self):
        pass

    def test_updating_bookmark(self):
        pass


class TestDeletes(APITestCase):

    def setUp(self):
        self.client.force_authenticate(user=user)
        self.bookmark = BookmarkFactory.build()

    def test_deleting_a_bookmark(self):
        pass

    #TODO: make sure that a tag is deleted when you delete the last bookmark that included it
    #TODO: test that disallowed methods are truly disallowed:
    #       - e.g. you cannot create Tags directly, only through creation of a Bookmark