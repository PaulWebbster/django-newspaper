# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from models.news import News
from models.plugins import ArticlesListPlugin


class CMSArticlesListPlugin(CMSPluginBase):
    model = ArticlesListPlugin  # model where plugin data are saved
    module = _("Aktualnosci")
    name = _("Wtyczka - lista najnowszych artykulow")  # name of the plugin in the interface
    render_template = "django_newspaper/plugins/new_articles.html"

    def render(self, context, name, placeholder):
        context['arts'] = News.objects.all()[:10]

        return context


plugin_pool.register_plugin(CMSArticlesListPlugin)
