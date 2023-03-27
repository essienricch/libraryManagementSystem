from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.BookCreateApiView.as_view(), name='book'),
    path('books/', views.book_list, name='book'),
    path('update/<int:pk>/', views.update_book_list, name='update'),
    path('delete/<int:pk>/', views.delete_book_list, name='delete'),
    path('', views.get_authors, name='author'),
    path('author/', views.AuthorCreate, name='create_author')
]
