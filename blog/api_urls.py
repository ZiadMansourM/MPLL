from django.urls import path, include
from .api_views import (
        CommmentJsonCreateView,
        CommmentJsonListView
    )


urlpatterns = [
    path('<uuid:pk>/comment/create', CommmentJsonCreateView.as_view(), name='api-comment-create'),
    path('<uuid:pk>/comment/', CommmentJsonListView.as_view(), name='api-comment-list'),
]
