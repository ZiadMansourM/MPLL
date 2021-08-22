from django.urls import path, include
from .api_views import (
        CommmentJsonCreateView,
        CommmentJsonListView,
        ReplyJsonCreateView
    )


urlpatterns = [
    path('<uuid:pk>/comment/new', CommmentJsonCreateView.as_view(), name='api-comment-create'),
    path('<uuid:pk>/comment/', CommmentJsonListView.as_view(), name='api-comment-list'),
    path('<uuid:pk>/comment/<uuid:id>/reply/new', ReplyJsonCreateView.as_view(), name='api-reply-create'),
]
