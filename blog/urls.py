from django.urls import path, include
from .views import (
    contact_us,
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    CommentCreateView,
    ReplyCreateView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('contactus/', contact_us, name="contact-us"),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:pk>/comment/<int:id>', ReplyCreateView.as_view(), name='reply-create'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('new/', PostCreateView.as_view(), name='blog-create')
]
