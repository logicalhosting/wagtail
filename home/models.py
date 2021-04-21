from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel

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


