from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from wagtailnews.models import NewsIndexMixin, AbstractNewsItem, AbstractNewsItemRevision
from wagtailnews.decorators import newsindex

from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel


# The decorator registers this model as a news index
@newsindex
class NewsIndex(NewsIndexMixin, Page):
    # Add extra fields here, as in a normal Wagtail Page class, if required
    newsitem_model = 'NewsItem'


class NewsItem(AbstractNewsItem):
    # NewsItem is a normal Django model, *not* a Wagtail Page. RichTextField
    # Add any fields required for your page.
    # It already has ``date`` field, and a link to its parent ``NewsIndex`` Page
    title = models.CharField(max_length=255)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('svg', SvgChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True)

    panels = [
        FieldPanel('title', classname='full title'),
        StreamFieldPanel('body', classname='full'),
    ] + AbstractNewsItem.panels

    def __str__(self):
        return self.title


class NewsItemRevision(AbstractNewsItemRevision):
    newsitem = models.ForeignKey(NewsItem, related_name='revisions', on_delete=models.CASCADE)

