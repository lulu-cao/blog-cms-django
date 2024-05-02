from django_filters import rest_framework as filters
from django.http import JsonResponse
from rest_framework.decorators import action
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from . import models, serializers, tasks
import json

class RssFeedFilter(filters.FilterSet):
    user = filters.NumberFilter(field_name='user', lookup_expr='exact')
    url = filters.CharFilter(field_name='url', lookup_expr='exact')

class RssFeedViewSet(viewsets.ModelViewSet):
    queryset = models.RssFeed.objects.all()
    serializer_class = serializers.RssFeedSerializer
    filterset_class = RssFeedFilter


class FeaturedArticleViewSet(viewsets.ModelViewSet):
    queryset = models.FeaturedArticle.objects.all()
    serializer_class = serializers.FeaturedArticleSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


@csrf_exempt
@require_http_methods(['POST'])
def cache_rss_feed(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body.decode('utf-8'))
        else:
            data = request.POST
        url = data.get('url')
        user_id = data.get('user')

        if not url or not user_id:
            return JsonResponse({'error': 'url and user required'}, status=400)

        if models.RssFeed.objects.filter(url=url, user_id=user_id).exists():
            return JsonResponse({'error': 'Feed already cached for this user'}, status=409)

        tasks.cacheUserFeeds(user_id, url)
        return JsonResponse({'status': 'success'}, status=201)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
@require_http_methods(['POST'])
def cache_featured_articles(request):
    tasks.cacheFeaturedArticles()
    return JsonResponse({'status': 'success'}, status=201)
