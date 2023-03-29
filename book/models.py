from enum import Enum
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=True, null=False)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} -> {self.last_name}'


class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)


class Book(models.Model):
    GENRE_CHOICES = [
        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('ROMANCE', 'ROM'),
        ('SPORT', 'SPO'),
        ('ENTERTAINMENT', 'ENT'),
    ]

    LANGUAGE_CHOICES = [
        ('NORWAY', 'NOR'),
        ('FINLAND', 'FIN'),
        ('ENGLAND', 'ENG'),
        ('GHANA', 'GHA'),
    ]
    title = models.CharField(max_length=250, blank=False, null=False)
    isbn = models.CharField(max_length=20, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES, default='ROM')
    price = models.DecimalField(max_digits=6, default=0, decimal_places=2)
    language = models.CharField(max_length=255, choices=LANGUAGE_CHOICES, default='FIN')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title


# class Genre(models.Model):
#
#
#
#     def __str__(self):
#         return self.genre_name
#
#
# class Language(models.Model):
#
#
#
#
#     def __str__(self):
#         return self.language_name


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'A'),
        ('BORROWED', 'B')
    ]

    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=False)
    imprint = models.CharField(max_length=55, null=False, blank=False)
    borrower = models.OneToOneField(LibraryUser, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.imprint
