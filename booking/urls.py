from django.urls import path, include
from .views import (AuthorCreateView, AuthorDeleteView, AuthorUpdateView, BookCreateView, BookListView, BookDetailView, BookDeleteView, BookUpdateView,
                    AuthorListView, PublisherCreateView, PublisherDeleteView, PublisherListView, PublisherUpdateView)
urlpatterns = [
    path('', BookListView.as_view(), name='booking-home'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('new/', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    ###########################
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/new/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/',
         AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/',
         AuthorDeleteView.as_view(), name='author-delete'),
    ###########################
    path('publishers/', PublisherListView.as_view(), name='publisher-list'),
    path('publishers/new/', PublisherCreateView.as_view(), name='publisher-create'),
    path('publishers/<int:pk>/update/',
         PublisherUpdateView.as_view(), name='publisher-update'),
    path('publishers/<int:pk>/delete/',
         PublisherDeleteView.as_view(), name='publisher-delete'),
]
