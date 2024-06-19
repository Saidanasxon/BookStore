from django.urls import path
from . import views
app_name = 'admins'

urlpatterns = [
    # Sellers
    path('sellers_list/', views.SellersView.as_view(), name='sellers_list'),
    path('add_seller/', views.AddSellerView.as_view(), name='add_seller'),
    path('edit_seller/<int:seller_id>/', views.EditSellerView.as_view(), name='edit_seller'),
    path('delete_seller/<int:seller_id>/', views.DeleteSellerView.as_view(), name='delete_seller'),
    # Categories
    path('category_list/', views.BookCategoriesView.as_view(), name='book_categories'),
    path('add_category/', views.AddBookCategoryView.as_view(), name='add_category'),
    path('edit_category/<int:category_id>/', views.EditBookCategoryView.as_view(), name='edit_category'),
    path('delete_category/<int:category_id>/', views.DeleteBookCategoryView.as_view(), name='delete_category'),
    # Genres
    path('genre_list/', views.BookGenresView.as_view(), name='book_genres'),
    path('add_genre/', views.AddBookGenreView.as_view(), name='add_genre'),
    path('edit_genre/<int:genre_id>/', views.EditBookGenreView.as_view(), name='edit_genre'),
    path('delete_genre/<int:genre_id>/', views.DeleteBookGenreView.as_view(), name='delete_genre'),
    # Clients
    path('clients_list/', views.ClientsView.as_view(), name='clients_list'),
    path('delete_client/<int:client_id>/', views.DeleteClientView.as_view(), name='delete_client'),
    path('edit_client/<int:client_id>/', views.EditClientView.as_view(), name='edit_client'),
]