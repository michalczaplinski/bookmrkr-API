from django.utils import timezone
from haystack import indexes
from .models import Bookmark


class BookmarkIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    description = indexes.CharField(model_attr='description')
    content = indexes.CharField(model_attr='content')

    autocomplete = indexes.EdgeNgramField()

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.title, obj.description, obj.content
        ))

    def get_model(self):
        return Bookmark

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_created__lte=timezone.now())