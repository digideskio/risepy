from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.article, name='article'),
    url(r'^score/(?P<series_id>[0-9]+)/(?P<match_id>[0-9]+)/$', views.score, name='score'),
    url(r'^comments/', include('django_comments.urls')),
]