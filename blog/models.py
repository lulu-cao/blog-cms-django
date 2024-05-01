from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=200)

    def __str__(self):
        return self.uid

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

class FeaturedArticle(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    published = models.DateTimeField(blank=True, null=True)
    link = models.URLField()
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

    def Meta():
        ordering = ['order']

class RssFeed(models.Model):
    url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rss_feeds')

    def __str__(self):
        return self.url

class RssCache(models.Model):
    feed = models.ForeignKey(RssFeed, on_delete=models.CASCADE, related_name='rss_cache')
    title = models.CharField(max_length=200)
    summary = models.TextField()
    published = models.DateTimeField(blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.title
