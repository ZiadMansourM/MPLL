from django.urls import path, include
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('new/', PostCreateView.as_view(), name='blog-create'),
]
