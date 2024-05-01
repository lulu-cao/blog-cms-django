from django.contrib import admin
from . import models

class RssCacheInline(admin.StackedInline):
  model = models.RssCache
  extra = 0

@admin.register(models.RssFeed)
class RssFeedAdmin(admin.ModelAdmin):
  inlines = [RssCacheInline]

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
  pass

@admin.register(models.FeaturedArticle)
class FeaturedArticleAdmin(admin.ModelAdmin):
  pass

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
  pass
