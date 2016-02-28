from django.conf.urls import url
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'bookmarks/$', views.bookmarks),
    url(r'^$', views.index),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

