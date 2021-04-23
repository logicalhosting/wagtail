from django.db import models

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock(max_length=128)
    surname = blocks.CharBlock(max_length=256)
    photo = ImageChooserBlock(required=False)
    biography = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/person_block.html'
        icon = 'user'
