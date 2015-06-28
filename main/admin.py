from django.contrib import admin

# Register your models here.
from .models import Bookmark, Tag

admin.site.register(Bookmark)
admin.site.register(Tag)
