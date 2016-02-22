from django.conf.urls import url

from views.news import NewsBaseView
from views.news import NewsListView
from views.author import AuthorDetail

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', NewsBaseView.as_view(), name='news_detail'),
    url(r'^list/$', NewsListView.as_view(), name='news_list'),
    url(r'^author/(?P<pk>\d+)/$', AuthorDetail.as_view(), name='author_detail'),
]
