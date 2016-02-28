# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models


class ArticlesListPlugin(CMSPlugin):
    events_number = models.IntegerField("Liczba wyświetlanych artykulow", default=10)
