from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from ..models.news import News
from ..models.news import Author
from django.contrib.auth.models import User
import datetime

NEWS_PER_PAGE = 10

class NewsBaseView(View):
    """
    Base view for view of news
    """
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsBaseView, self).get_context_data(**kwargs)
        authors = Author.objects.all()

        return context

class NewsDetailView(DetailView):
    model = News

class NewsListView(NewsBaseView, ListView):
    model = News
    paginate_by = NEWS_PER_PAGE

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)

        return context

class NewsArchivalListView(ListView):
    #template_name = 'books/books_by_publisher.html'
    model = News
    paginate_by = NEWS_PER_PAGE
    template_name = "django_newspaper/arch_news_list.html"

    def get_queryset(self):
        if 'day' in self.kwargs:
            requested_date = datetime.date(int(self.kwargs['year']), int(self.kwargs['month']), int(self.kwargs['day']))
            return News.objects.all().filter(pub_date__contains=requested_date)
        elif 'month' in self.kwargs:
            return News.objects.all().filter(pub_date__year=self.kwargs['year'], pub_date__month=self.kwargs['month'])
        elif 'year' in self.kwargs:
            return News.objects.all().filter(pub_date__year=self.kwargs['year'])

    def get_context_data(self, **kwargs):
        context = super(NewsArchivalListView, self).get_context_data(**kwargs)

        link = ""

        if 'year' in self.kwargs:
            link += "%s/" % self.kwargs['year']
        if 'month' in self.kwargs:
            link += "%s/" % self.kwargs['month']
        if 'day' in self.kwargs:
            link += "%s/" % self.kwargs['day']

        context['link'] = link

        return context
