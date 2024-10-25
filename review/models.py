from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return self.title


class Review(models.Model):

    book = models.ForeignKey(Book, related_name='review', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"

    def __str__(self):
        return f'Review for the book {self.book.title}'