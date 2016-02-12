from django.contrib import admin
from models import News
# Register your models here.
from django.utils.translation import ugettext_lazy as _


class AdminNews(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_is_visible', 'pub_date')
    list_filter = ('author', 'pub_date', 'status')

    def get_is_visible(self, entry):
        return entry.is_visible

    get_is_visible.boolean = True
    get_is_visible.short_description = _('Widoczny')

admin.site.register(News, AdminNews)
