from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
router.register('book-instance', views.BookInstanceSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('books/', views.GetBookViews.as_view(), name='book_list'),
    # path('authors/', views.GetAuthorView.as_view()),
    # path('books/', views.book_list, name='book'),
    # path('book-instance/<int:pk>/', views.BookInstanceSet.as_view()),
    path('authors/<int:pk>/', views.an_author_detail, name='author_detail'),
    path('author/<int:pk>/', views.GetAuthorDetailView.as_view()),
    path('book/<int:pk>/', views.GetBookDetailView.as_view()),
    path('create_book/', views.CreateBookView.as_view()),
    path('create_author/', views.CreateAuthorView.as_view()),

]
