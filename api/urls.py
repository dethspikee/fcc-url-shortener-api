from django.conf.urls import url

from .views import Index, UrlShortener, UrlCreate

urlpatterns = [
    url(r'^api/shorturl/new/?$', UrlCreate.as_view()),
    url(r'^api/shorturl/(?P<id>\d+)/?$', UrlShortener.as_view()),
    url(r'^$', Index.as_view()),
]