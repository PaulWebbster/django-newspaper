# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _


class Author(User):
    class Meta:
        proxy = True

    @property
    def is_author(self):
        return True

    def __unicode__(self):
        return self.get_full_name()


class News(models.Model):
    SZKIC = 0
    OPUBLIKOWANY = 1

    STATUS_CHOICES = (
        (SZKIC, _('Szkic')),
        (OPUBLIKOWANY, _('Opublikowany'))
    )

    status = models.IntegerField(_("Status"), max_length=1, choices=STATUS_CHOICES)
    title = models.CharField(_("Tytuł"), max_length=255)
    lead = RichTextUploadingField(_("Akapit wiodący"))
    article = RichTextUploadingField(_("Tekst główny"), blank=True)
    pub_date = models.DateTimeField(_("Data publikacji"))
    author = models.ForeignKey(Author, verbose_name=_("Autor"))

    @property
    def is_visible(self):
        return True if self.status == self.OPUBLIKOWANY else False

    def save_model(self, request, instance, form, change):
        self.author = request.user
        return instance

#    visible = property(visible_property)

    class Meta:
        verbose_name = _("Wiadomość")
        verbose_name_plural = _("Wiadomości")
        ordering = ["-pub_date"]
