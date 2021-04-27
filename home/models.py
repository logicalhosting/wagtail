from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel

from wagtailcolumnblocks.blocks import ColumnsBlock

class HomePage(Page):
    hero_title = models.CharField(
        max_length=120,
        blank=True,
        help_text="Main text displayed in the hero section over the background."
    )

    hero_subtitle = models.TextField(
        max_length=200,
        blank=True,
        help_text="Subtitle following the main title in the hero section."
    )

    cta_btn_text = models.CharField(
        max_length=64,
        blank=True,
        default="Learn More",
        help_text="Call-To-Action Button Text",
    )

    cta_btn_link = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="Internal page link to send the user to when clicking CTA button."
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("cta_btn_text"),
        PageChooserPanel("cta_btn_link"),
    ] 


class LpContentBlocks(blocks.StreamBlock):
    """
    The blocks you want to allow within each MyColumnBlocks column.
    """

    image = ImageChooserBlock()
    text = blocks.CharBlock()


class LpColumnBlocks(blocks.StreamBlock):
    """
    All the root level blocks you can use
    """
    column_2_1 = ColumnsBlock(
        # Blocks you want to allow within each column
        LpContentBlocks(),
        # Two columns in admin, first twice as wide as the second
        ratios=(1, 1),
        # Used for grouping related fields in the streamfield field picker
        group="Columns",
        # 12 column frontend grid (this is the default, so can be omitted)
        grid_width=12,
        # Override the frontend template
        template='blocks/two_column_block.html',
    )


class SidebarPage(Page):
    content = fields.StreamField(LpColumnBlocks)

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('content')
    ]

