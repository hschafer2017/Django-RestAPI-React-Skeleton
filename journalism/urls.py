from django.conf.urls import url, include
from django.urls import path
from journalism import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Article API')
publication_view = get_schema_view(title='Publication API')

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'articles', views.ArticleViewSet, base_name='articles')
# router.register(r'publications', views.PublicationViewSet,
# base_name='publications')

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/publications/', views.PublicationListCreate.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('publication/', publication_view),
    path('schema/', schema_view),
]