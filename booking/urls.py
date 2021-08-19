from django.urls import path, include
from .views import BookCreateView, BookListView ,BookDetailView,BookDeleteView,BookUpdateView
urlpatterns = [
    path('', BookListView.as_view(), name='booking-home'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('new/',BookCreateView.as_view(),name='book-create'),
    path('<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    path('<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
]
