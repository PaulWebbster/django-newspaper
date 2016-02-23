# -*- coding: utf-8 -*-
from django import template
from ..models.news import News
from ..models.news import Author

register = template.Library()


@register.inclusion_tag("django_newspaper/sidebar/authors.html")
def show_authors():
    context_dict = dict()
    authors_list = []

    for author in Author.objects.all():
        if author.is_author:
            authors_list.append(author)

    context_dict['authors'] = authors_list

    return context_dict
