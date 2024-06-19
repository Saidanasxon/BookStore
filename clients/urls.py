from django.urls import path
from . import views
app_name = 'clients'

urlpatterns = [
    path('store/', views.BooksView.as_view(), name='store'),
    path('book/<int:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('delete_cart/<int:book_id>/', views.delete_from_cart, name='delete'),
]