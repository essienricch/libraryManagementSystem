from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from book.models import Book, Author
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, BookUpdateSerializer, \
    AuthorCreateSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializers = BookSerializer(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        book = BookCreateSerializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response('Book saved successfully', status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_book_list(request, pk):
    my_book = get_object_or_404(Book, pk=pk)
    serializer = BookUpdateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        my_book.update(Book, serializer)
        return Response("Book Update Successful")
    else:
        return Response(serializer.errors, status=403)


# @api_view(['DELETE'])
# def delete_book_list(request, pk):
#     if request.method == 'DELETE':
#         my_book = Book.objects.get(pk)
#         return Response(Book.delete(my_book), 'Book deleted successfully')


@api_view(['DELETE'])
def delete_book_list(pk):
    my_book = get_object_or_404(Book, pk=pk)
    serialized = BookSerializer(my_book)
    return Response(serialized.Meta, 'Book deleted successfully')


@api_view()
def get_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def author_detail(request, pk):
    if request.method == 'GET':
        author = get_object_or_404(Author, pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    elif request.method == 'PUT':
        author = get_object_or_404(Author, id)
        serialized_data = AuthorSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        author.update(Author, serialized_data)
        return Response('Author updated', serialized_data.Meta)


class BookCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer(Book, queryset)


class AuthorCreateApiView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer(Author, queryset)


@api_view(['POST'])
def AuthorCreate(request):
    serializers = AuthorCreateSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
    return Response('Author created successfully', status=status.HTTP_201_CREATED)


