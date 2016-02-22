from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View
from ..models.news import News
from ..models.news import Author
from django.contrib.auth.models import User

class NewsBaseView(View):
    """
    Base view for view of news
    """
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsBaseView, self).get_context_data(**kwargs)
        authors = Author.objects.all()

        return context


class NewsListView(NewsBaseView, ListView):
    model = News
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)

        return context