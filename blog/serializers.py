from rest_framework import serializers
from .models import models

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = '__all__'
