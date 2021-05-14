from django.db import models
from django import forms
from django.http import HttpResponse

from wagtail.core.blocks import (
    CharBlock,
    FieldBlock,
    ListBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    ChoiceBlock,
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
        form_classname = 'person-block struct-block'
        template = 'blocks/person_block.html'
        icon = 'user'


BUTTON_TYPE_CHOICES = (
    ('mdc-button', "Text Only"),
    ('outlined', "Outline"),
    ('raised', "Solid Raised"),
)

class ButtonBlock(StructBlock):
    button_text = CharBlock(max_length=64)
    button_type = ChoiceBlock(
        choices=[
            ('mdc-button', 'Text Only'),
            ('outlined', 'Outline'),
            ('raised', 'Solid Raised'),
        ])

    class Meta:
        template = 'blocks/button_block.html'
        icon = 'user'
