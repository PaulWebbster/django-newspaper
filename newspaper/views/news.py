from django.views.generic.detail import DetailView
from ..models.news import News


class NewsBaseView(DetailView):
    """
    Base view for view of news
    """
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsBaseView, self).get_context_data(**kwargs)

        return context
