# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..models.news import News
from ..models.news import Author
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView


class AuthorDetail(SingleObjectMixin, ListView):
    paginate_by = 5
    template_name = "django_newspaper/author_detail.html"
    model = News

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super(AuthorDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AuthorDetail, self).get_context_data(**kwargs)
        context['author'] = self.object
        return context

    def get_queryset(self):
        return self.object.news_set.all()


class AuthorList(ListView):
    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)

        return context
