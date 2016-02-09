from __future__ import unicode_literals

from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    STATUS_CHOICES = (
        (0, 'szkic'),
        (1, 'opublikowany')
    )

    status = models.IntegerField("Status", max_length=1, choices=STATUS_CHOICES)
    lead = HTMLField("Akapit wiodacy")
    news_text = HTMLField("Pelen tekst")
    pub_date = models.DateTimeField("Data publikacji")
    autor = models.OneToOneField(User)
