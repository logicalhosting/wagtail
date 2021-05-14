from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks

from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from wagtailnews.decorators import newsindex
from wagtailnews.models import NewsIndexMixin, AbstractNewsItem, AbstractNewsItemRevision

from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel

from core.blocks import PersonBlock, ButtonBlock


# The decorator registers this model as a news index
@newsindex
class NewsIndex(NewsIndexMixin, Page):
    # Add extra fields here, as in a normal Wagtail Page class, if required
    newsitem_model = 'NewsItem'

class NewsItem(AbstractNewsItem):
    # NewsItem is a normal Django model, *not* a Wagtail Page. RichTextField
    # Add any fields required for your page.
    # It already has ``date`` field, and a link to its parent ``NewsIndex`` Page
    headline = models.CharField(max_length=255)
    byline = models.CharField(max_length=255)
    lead = StreamField([
        ('lead', blocks.RichTextBlock()),
    ], blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('blockquote', blocks.BlockQuoteBlock()),
        ('svg', SvgChooserBlock()),
        ('image', ImageChooserBlock()),
        ('embed', EmbedBlock()),
        ('button', ButtonBlock()),
    ], blank=True)
    author = StreamField([
        ('author', PersonBlock()),
    ], blank=True)

    panels = [
        FieldPanel('headline', classname='full title'),
        FieldPanel('byline', classname='byline'),
        StreamFieldPanel('lead', classname='lead'),
        StreamFieldPanel('body', classname='body'),
        StreamFieldPanel('author', classname='author'),
    ] + AbstractNewsItem.panels

    def __str__(self):
        return self.headline


class NewsItemRevision(AbstractNewsItemRevision):
    newsitem = models.ForeignKey(NewsItem, related_name='revisions', on_delete=models.CASCADE)

