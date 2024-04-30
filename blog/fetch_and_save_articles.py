import feedparser
from .models import FeaturedArticle
from django.utils.dateparse import parse_datetime

def fetch_and_save_articles():
    feed_url = 'https://medium.com/feed/@lcao_5526'
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        # Check if article already exists to avoid duplicates
        if not FeaturedArticle.objects.filter(link=entry.link).exists():
            article = FeaturedArticle(
                title=entry.title,
                summary=entry.summary,
                published=parse_datetime(entry.published),
                link=entry.link
            )
            article.save()


