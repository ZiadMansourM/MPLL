from django.urls import path, include
from .views import BookListView ,BookDetailView
urlpatterns = [
    path('', BookListView.as_view(), name='booking-home'),
    path('<int:pk>/', BookDetailView.as_view(), name='booking-detail'),
]
