from rest_framework import serializers
from . import models

class RssCacheSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RssCache
        fields = '__all__'

class RssFeedSerializer(serializers.ModelSerializer):

    rss_cache = RssCacheSerializer(many=True, read_only=True)

    class Meta:
        model = models.RssFeed
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = '__all__'

class FeaturedArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FeaturedArticle
        fields = '__all__'
