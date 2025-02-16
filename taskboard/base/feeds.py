from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Task as NewsItem


class LatestEntriesFeed(Feed):
    title = "Taskboard"
    link = "/latest/feed/"
    description = "Updates on changes and additions to taskboard."

    
    def items(self):
        return NewsItem.objects.order_by("-pub_date")[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description

    # # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse("news-item", args=[item.pk])