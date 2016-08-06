from django.utils import timezone
from haystack import indexes
from .models import Bookmark


class BookmarkIndex(indexes.SearchIndex, indexes.Indexable):

    id = indexes.IntegerField(model_attr='id')

    text = indexes.EdgeNgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    content = indexes.CharField(model_attr='content')
    owner = indexes.CharField(model_attr='owner')


    def get_model(self):
        return Bookmark

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_created__lte=timezone.now())