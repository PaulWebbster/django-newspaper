# -*- coding: utf-8 -*-
from django import template
from ..models.news import News
from ..models.news import Author
import calendar
import datetime
import math

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


@register.inclusion_tag("django_newspaper/sidebar/calendar.html")
def show_calendar():
    context_dict = dict()

    now = datetime.datetime.now()
    month_days = calendar.monthrange(now.year, now.month)[1]
    first_day = datetime.datetime(now.year, now.month, 1)
    offset = first_day.weekday()

    weeks = math.ceil(month_days/7.)

    context_dict['days'] = month_days
    context_dict['first_day'] = first_day.weekday()

    calendar_str = ""
    day_num = 1

    for week in range(int(weeks)):
        calendar_str += "<tr>"
        for day in range(7):
            if day_num < 28:
                news_number = len(News.objects.all().filter(pub_date__contains=datetime.date(now.year, now.month,
                                                                                             day_num)))
            if week == 0:
                if day >= offset:
                    if news_number == 0:
                        calendar_str += "<td>{}</td>".format(day_num)
                    else:
                        calendar_str += "<td><a href='/news/list/{year}/{month}/{day}/'>" \
                                        "{day}</a></d>".format(year=now.year, month=now.month, day=day_num)
                    day_num += 1
                else:
                    calendar_str += "<td></td>"
            else:
                if day_num <= month_days:
                    if news_number == 0:
                        calendar_str += "<td>{}</td>".format(day_num)
                    else:
                        calendar_str += "<td><a href='/news/list/{year}/{month}/{day}/'>" \
                                        "{day}</a></d>".format(year=now.year, month=now.month, day=day_num)
                    day_num += 1
                else:
                    calendar_str += "<td></td>"
        calendar_str += "</tr>"

    context_dict['tbody'] = calendar_str

    return context_dict

