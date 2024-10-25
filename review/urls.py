from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList.as_view(), name='all_books'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('books/<int:book_id>/reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail')
]