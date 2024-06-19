from django.urls import path
from . import views
app_name = 'sellers'

urlpatterns = [
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:book_id>/', views.EditBookView.as_view(), name='edit_book'),
    path('delete_book/<int:book_id>/', views.DeleteBookView.as_view(), name='delete_book'),
    path('my_books/', views.MyBooksView.as_view(), name='my_books'),
]