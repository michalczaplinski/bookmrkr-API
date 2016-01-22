from django.contrib.auth.models import User
from django.db import models
from colorful.fields import RGBColorField


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    color = RGBColorField(null=True,
                          colors=['#FFFFFF',
                                  '#E91E63',
                                  '#9C27B0',
                                  '#673AB7',
                                  '#3F51B5',
                                  '#2196F3',
                                  '#03A9F4',  # light blue
                                  '#00BCD4',  # cyan
                                  '#009688',  # teal
                                  '#4CAF50',  # green
                                  '#8BC34A',  # light green
                                  '#CDDC39',  # lime
                                  '#FFEB3B',  # yellow
                                  '#FFC107',  # amber
                                  '#FF9800',  # orange
                                  '#FF5722',  # deep orange
                                  '#795548',  # brown
                                  '#9E9E9E',  # grey
                                  '#607D8B',  # blue gray
                                  '#000000',  # black
                                  '#FFFFFF',   # white
                                  ])

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Bookmark(models.Model):

    ARTICLE = 'Article'
    LINK = 'Link'
    IMAGE = 'Image'
    VIDEO = 'Video'

    BOOKMARK_TYPE_CHOICES = (
        (LINK, 'Link'),
        (ARTICLE, 'Article'),
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
    )

    url = models.URLField()
    title = models.CharField('title', max_length=50)
    cover = models.ImageField(blank= True, null=True)
    description = models.TextField('description', blank=True)
    content = models.TextField('content', blank=True)
    date_created = models.DateTimeField('date created', auto_now=True)
    date_updated = models.DateTimeField('date updated', auto_now=True)
    owner = models.ForeignKey(User, related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)
    type = models.CharField(max_length=10,
                            choices=BOOKMARK_TYPE_CHOICES,
                            default=LINK)
    is_trashed = models.BooleanField(default=False)

    # like on reddit, eg. 'github.com'
    domain = models.CharField('domain', max_length=40, blank=True)

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)
