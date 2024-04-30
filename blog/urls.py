from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'blogs', views.BlogViewSet)
router.register(r'featured-articles', views.FeaturedArticleViewSet)
