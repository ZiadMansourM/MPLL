from django.urls import path, include
from .api_views import (
        CommmentJsonCreateView,
        CommmentJsonListView,
        PostJsonLikeView,
        PostJsonUnlikeView,
        ReplyJsonCreateView,
        CommentJsonLikeView,
        CommentJsonUnlikeView,
        ReplyJsonLikeView,
        ReplyJsonUnlikeView
    )


urlpatterns = [
    path('<uuid:pk>/comment/new', CommmentJsonCreateView.as_view(), name='api-comment-create'),
    path('<uuid:pk>/comment/', CommmentJsonListView.as_view(), name='api-comment-list'),
    path('<uuid:pk>/comment/<uuid:id>/reply/new', ReplyJsonCreateView.as_view(), name='api-reply-create'),
    path('<uuid:pk>/like/', PostJsonLikeView.as_view(), name='api-like-post'),
    path('<uuid:pk>/unlike/', PostJsonUnlikeView.as_view(), name='api-unlike-post'),
    path('<uuid:pk>/comment/<uuid:id>/like', CommentJsonLikeView.as_view(), name='api-like-comment'),
    path('<uuid:pk>/comment/<uuid:id>/unlike', CommentJsonUnlikeView.as_view(), name='api-unlike-comment'),
    path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>/like', ReplyJsonLikeView.as_view(), name='api-like-reply'),
    path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>/unlike', ReplyJsonUnlikeView.as_view(), name='api-unlike-reply'),
]
