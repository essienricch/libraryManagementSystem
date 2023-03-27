from rest_framework import serializers
from book.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # birth_day = serializers.DateField(source='date_of_birth')
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'description', 'author']

    # author = serializers.StringRelatedField()


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description']


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description']


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
