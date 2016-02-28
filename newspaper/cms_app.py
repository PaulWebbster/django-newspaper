# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ZawodyApp(CMSApp):
    name = _("Aktualnosci")  # give your app a name, this is required
    urls = ["django_newspaper.urls"]  # link your app to url configuration(s)
    app_name = "aktualnosci"

apphook_pool.register(ZawodyApp)  # register your app
