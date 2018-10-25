from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'vordem_blog.BlogPage', on_delete=models.CASCADE,
        related_name='tagged_items')


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogPage(Page):
    template = 'article.html'
    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    # Search index configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Editor panels configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
    ]

    promote_panels = [
        ImageChooserPanel('feed_image'),
        FieldPanel('tags'),
        MultiFieldPanel(Page.promote_panels, "SEO"),
    ]

