from django.shortcuts import render
from rest_framework import generics

from .serializers import BookSerializer, ReviewSerializer

from .models import Book, Review

# Create your views here.


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        """
        This view should return a list of all the reviews for
        the book as determined by the book_id portion of the URL.
        """
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book_id=book_id)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer