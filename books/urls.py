from django.urls import path
from . import views

urlpatterns = [
    path('books/new/', views.create_book, name='create_book'),
    path('books/<str:book_id>/create_comment/', views.create_comment, name='create_comment'),
    path('books/<str:book_id>/', views.book_detail, name='book_detail'),
    path('my-books/', views.my_books, name='my_books'),
    path('books/<str:book_id>/edit/', views.edit_book, name='edit_book'),
    path('books/<str:book_id>/delete/', views.delete_book, name='delete_book'),
]
