from django.shortcuts import render
from . import models, serializers

class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
