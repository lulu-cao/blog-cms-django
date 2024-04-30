from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = '__all__'

class FeaturedArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FeaturedArticle
        fields = '__all__'
