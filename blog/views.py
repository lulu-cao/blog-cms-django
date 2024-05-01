from rest_framework import viewsets
from . import models, serializers
from django_filters import rest_framework as filters

class RssFeedFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name='user', lookup_expr='exact')
    url = filters.CharFilter(field_name='url', lookup_expr='exact')

class RssFeedViewSet(viewsets.ModelViewSet):
    queryset = models.RssFeed.objects.all()
    serializer_class = serializers.RssFeedSerializer
    filterset_class = RssFeedFilter

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class FeaturedArticleViewSet(viewsets.ModelViewSet):
    queryset = models.FeaturedArticle.objects.all()
    serializer_class = serializers.FeaturedArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
