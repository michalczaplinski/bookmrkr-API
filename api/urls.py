from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^bookmarks/$', views.bookmark_list),
]
