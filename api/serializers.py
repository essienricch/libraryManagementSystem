from rest_framework import serializers
from book.models import Book, Author, BookInstance
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class AuthorSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=255)
    # last_name = serializers.CharField(max_length=255)
    # birth_day = serializers.DateField(source='date_of_birth')
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'discount_price', 'author']

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_detail',

    )

    discount_price = serializers.SerializerMethodField(method_name='discount')

    # date_added = serializers.DateTimeField(read_only=True)

    def discount(self, book: Book):
        return book.price * 25 / 100

    # author = serializers.StringRelatedField()


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'description', 'author']


# class BookUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['title', 'isbn', 'description']


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']


class UserCreate(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']


class UserSetSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'email', 'first_name', 'last_name']


class BookInstanceSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookInstance
        fields = ['user_id', 'due_back', 'status', 'book', 'imprint', 'borrower']
