from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book.models import Book, Author, LibraryUser, BookInstance
from .pagination import DefaultPageNumberPagination
from .permissions import IsAdminOrReadOnly
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, \
    AuthorCreateSerializer, BookInstanceSerializer

from rest_framework.permissions import IsAuthenticated


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


# @api_view(['PUT'])
# def update_book_list(request, pk):
#     my_book = get_object_or_404(Book, pk=pk)
#     serializer = BookUpdateSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         my_book.update(Book, serializer)
#         return Response("Book Update Successful")
#     else:
#         return Response(serializer.errors, status=403)


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


@api_view(['POST'])
def AuthorCreate(request):
    serializers = AuthorCreateSerializer(data=request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save()
    return Response('Author created successfully', status=status.HTTP_201_CREATED)


class GetBookViews(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class GetAuthorView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GetAuthorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GetBookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateAuthorView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer


class CreateBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


@api_view()
def an_author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookInstanceSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
