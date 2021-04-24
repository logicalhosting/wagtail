from django import forms

from wagtail.core.blocks import (
    CharBlock,
    FieldBlock,
    ListBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock

class PersonBlock(StructBlock):
    first_name = CharBlock(max_length=128)
    surname = CharBlock(max_length=256)
    photo = ImageChooserBlock(required=False)
    biography = RichTextBlock()

    class Meta:
        template = 'blocks/person_block.html'
        icon = 'user'


