from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="article-detail")

    class Meta:
        model = Article
        fields = ('url', 'id', 'title',
                  'content', 'image', 'published_date')
