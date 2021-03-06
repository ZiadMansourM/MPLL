from django.urls import path, include
from .views import (
    DeleteComment,
    DeleteReply,
    reportCreate,
    contact_us,
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    CommentDetailView,
    ReplyDetailView,
    ReportListView,
    PostLikeView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('new/', PostCreateView.as_view(), name='blog-create'),
    path('<uuid:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('<uuid:pk>/like/', PostLikeView, name='like-post'),
    path('<uuid:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('<uuid:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('<uuid:pk>/comment/<uuid:id>', CommentDetailView.as_view(), name='Comment-detail'),
    path('<uuid:pk>/comment/<uuid:id>/delete', DeleteComment, name='comment-delete'),
    path('<uuid:pk>/comment/<uuid:id>/reply/<uuid:num>', ReplyDetailView.as_view(), name='Comment-detail'),
    path('<uuid:pID>/comment/<uuid:cID>/reply/<uuid:rID>/delete', DeleteReply, name='reply-delete'),
    path('report/',ReportListView.as_view(),name='report-list'),
    path('report/new', reportCreate, name="report"),
    path('contactus/', contact_us, name="contact-us"),
]
