from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ArticleSerializer
from .models import Article


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'article': reverse('article-list', request=request, format=format)
    })


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get_object(self):
        obj = get_object_or_404(Article.objects.all(), pk=self.kwargs['pk'])
        return obj
