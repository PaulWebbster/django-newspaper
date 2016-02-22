from django.contrib import admin

from models.news import News
from django.utils.translation import ugettext_lazy as _


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_is_visible', 'pub_date')
    list_filter = ('author', 'pub_date', 'status')

    @staticmethod
    def get_is_visible(entry):
        return entry.is_visible

    def get_changeform_initial_data(self, request):
        """
        Provide initial datas when creating an entry
        """
        get_data = super(NewsAdmin, self).get_changeform_initial_data(request)
        get_data['author'] = request.user.pk
        return get_data


admin.site.register(News, NewsAdmin)
