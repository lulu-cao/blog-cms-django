import feedparser
from . import models
from django.utils.dateparse import parse_datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cacheFeaturedArticles():
    def cache(feed_url):
        feed = feedparser.parse(feed_url)
        # for key in feed.entries[0].keys():
        #     print(key)
        for entry in feed.entries:
            try:
                if not models.FeaturedArticle.objects.filter(link=entry.link).exists():
                    article = models.FeaturedArticle(
                        title=entry.title,
                        summary=entry.summary,
                        published=parse_datetime(entry.published),
                        link=entry.link
                    )
                    article.save()

            except ValueError as e:
                logging.error(f"Error parsing date for entry {entry.link}: {e}")
            except Exception as e:
                logging.error(f"An error occurred while processing entry {entry.link}: {e}")


    cache('https://medium.com/feed/@lcao_5526')
    # cache('https://www.goodreads.com/review/list_rss/134943772?shelf=read') # entry.user_review for summary

def cacheUserFeeds(user_id, feed_url):
    user = models.User.objects.get(pk=user_id)
    feed, created = models.RssFeed.objects.get_or_create(user=user, url=feed_url)
    rss_data = feedparser.parse(feed_url)

    for entry in rss_data.entries:
        if not models.RssCache.objects.filter(link=entry.link, feed=feed).exists():
            article = models.RssCache(
                feed=feed, # This is the foreign key
                title=entry.title,
                summary=entry.summary,
                # image=entry.image, # Haven't found a RSS feed that contains an image field
                published=parse_datetime(entry.published),
                link=entry.link
            )
            article.save()
