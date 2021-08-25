from django.urls import path, include
from .api_views import (
        AuthorCreateJsonView, 
        AuthorListJsonView, 
        PublisherCreateJsonView,
        CityCreateJsonView
    )


urlpatterns = [
    path('author/create/', AuthorCreateJsonView.as_view(), name='api-author-create'),
    path('publisher/create/', PublisherCreateJsonView.as_view(), name='api-publisher-create'),
    path('city/create/', CityCreateJsonView.as_view(), name='api-city-create'),
    path('author/', AuthorListJsonView.as_view(), name='api-author-list'),
]
