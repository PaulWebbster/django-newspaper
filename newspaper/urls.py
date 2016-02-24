from django.conf.urls import url

from views.news import NewsBaseView
from views.news import NewsListView
from views.news import NewsArchivalListView
from views.news import NewsDetailView
from views.author import AuthorDetail

urlpatterns = [
    url(r'^list/$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', NewsDetailView.as_view(), name='article-detail'),
    url(r'^list/(?P<year>[0-9]+)/$', NewsArchivalListView.as_view(), name='news_list_archival'),
    url(r'^list/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$', NewsArchivalListView.as_view(), name='news_list_archival'),
    url(r'^list/(?P<year>[0-9]+)/(?P<month>[0-9]+)/(?P<day>[0-9]+)/$', NewsArchivalListView.as_view(),
        name='news_list_archival'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author_detail'),
]
