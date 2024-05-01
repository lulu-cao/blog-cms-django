from rest_framework import viewsets
from . import models, serializers

class RssFeedViewSet(viewsets.ModelViewSet):
    queryset = models.RssFeed.objects.all()
    serializer_class = serializers.RssFeedSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class FeaturedArticleViewSet(viewsets.ModelViewSet):
    queryset = models.FeaturedArticle.objects.all()
    serializer_class = serializers.FeaturedArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
