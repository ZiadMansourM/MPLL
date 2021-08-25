from django.urls import path, include
from .views import (
    report,
    contact_us,
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    CommentCreateView,
    ReplyCreateView,
    CommentDetailView,
    ReplyDetailView,
    LikeView,
    CommentLikeView,
    ReplyLikeView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('contactus/', contact_us, name="contact-us"),
    path('report/', report, name="report"),
    path('<uuid:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('<uuid:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('<uuid:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>', ReplyDetailView.as_view(), name='Comment-detail'),
    path('<uuid:pk>/comment/<uuid:id>/reply', ReplyCreateView.as_view(), name='reply-create'),
    path('<uuid:pk>/comment/<uuid:id>', CommentDetailView.as_view(), name='Comment-detail'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('new/', PostCreateView.as_view(), name='blog-create'),
    path('like/<uuid:pk>/', LikeView, name='like-post'),
    path('<uuid:pk>/comment/<uuid:id>/like', CommentLikeView, name='like-comment'),
    path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>/like', ReplyLikeView, name='like-reply'),
]
