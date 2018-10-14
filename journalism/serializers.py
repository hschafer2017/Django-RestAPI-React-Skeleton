from rest_framework import serializers
from .models import Article, Publication


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content', 'image', 'published_date', 'publication')

class PublicationSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = ('name', 'affiliation', 'city', 'articles')
