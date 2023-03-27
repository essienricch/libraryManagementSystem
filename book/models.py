from enum import Enum
from uuid import uuid4

from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='0000-01-01')

    def __str__(self):
        return f'{self.first_name} -> {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    isbn = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genre')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, related_name='language')

    def __str__(self):
        return self.title


class Genre(models.Model):
    GENRE_CHOICES = [
        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('ROMANCE', 'ROM'),
        ('SPORT', 'SPO'),
        ('ENTERTAINMENT', 'ENT'),
    ]
    genre_name = models.CharField(max_length=15, choices=GENRE_CHOICES, default=None)

    def __str__(self):
        return self.genre_name


class Language(models.Model):
    LANGUAGE_CHOICES = [
        ('NORWAY',  'NOR'),
        ('FINLAND',  'FIN'),
        ('ENGLAND', 'ENG'),
        ('GHANA', 'GHA'),
    ]

    language_name = models.CharField(max_length=255, choices=LANGUAGE_CHOICES, default=None)

    def __str__(self):
        return self.language_name


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=None)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    imprint = models.CharField(max_length=55, null=False, blank=False)

    def __str__(self):
        return self.imprint
