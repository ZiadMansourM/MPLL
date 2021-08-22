from django.urls import path, include
from .api_views import (
        AuthorCreateJsonView, 
        AuthorListJsonView, 
        PublisherCreateJsonView
    )


urlpatterns = [
    path('author/create/', AuthorCreateJsonView.as_view(), name='api-author-create'),
    path('publisher/create/', PublisherCreateJsonView.as_view(), name='api-publisher-create'),
    path('author/', AuthorListJsonView.as_view(), name='api-author-list'),
]
