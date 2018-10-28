from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import (PublicationSerializer,
                          ArticleSerializer)
from .models import Publication, Article
from rest_framework import generics


class PublicationListCreate(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


# @api_view(['GET'])
# def publication_api_root(request, format=None):
#     return Response({
#         'publication': reverse('publication-list',
#                                request=request,
#                                format=format)
#         })

# @api_view(['GET'])
# def article_api_root(request, format=None):
#     return Response({
#         'article': reverse('article-list',
#                            request=request,
#                            format=format)
#     })


# class PublicationViewSet(viewsets.ModelViewSet):
#     serializer_class = PublicationSerializer
#     queryset = Publication.objects.all()

#     def get_object(self):
#         obj = get_object_or_404(Publication.objects.all(),
#                                 pk=self.kwargs['pk'])
#         return obj


# class ArticleViewSet(viewsets.ModelViewSet):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()

#     def get_object(self):
#         obj = get_object_or_404(Article.objects.all(),
#                                 pk=self.kwargs['pk'])
#         return obj

# Need to add an extra id for the article to link to publication?
