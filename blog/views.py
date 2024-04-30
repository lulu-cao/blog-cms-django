from rest_framework import viewsets
from . import models, serializers

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class FeaturedArticleViewSet(viewsets.ModelViewSet):
    queryset = models.FeaturedArticle.objects.all()
    serializer_class = serializers.FeaturedArticleSerializer
