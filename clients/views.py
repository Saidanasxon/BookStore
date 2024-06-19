from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from sellers.models import Book, BookCategory, BookGenre
from users.permissions import ClientRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import Cart, CartItem


class BooksView(View):
    def get(self, request):
        books = Book.objects.all()
        categories = BookCategory.objects.all()
        genres = BookGenre.objects.all()
        bestsellers = Book.objects.filter(is_bestseller=True)
        paginator = Paginator(books, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'books': books,
            'categories': categories,
            'genres': genres,
            'bestsellers': bestsellers,
            'page_obj': page_obj,
        }
        return render(request, 'clients/store.html', context)
    
class BookDetailView(View):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        related_books = Book.objects.filter(category=book.category).exclude(id=book_id)
        context = {
            'book': book,
            'related_books': related_books,
        }
        return render(request, 'clients/book_detail.html', context)
    
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST['cart'])

        if Cart.objects.filter(book=book).exists():
            cart = Cart.objects.filter(book=book).first()
            cart.quantity += quantity
            cart.save()
        else:
            cart = Cart()
            cart.book = book
            cart.quantity = quantity
            cart.save()

        return redirect('clients:store')
    
class CartView(View):
    def get(self, request):
        books = Cart.objects.all()
        context = {
            'books': books,
        }
        return render(request, 'clients/cart.html', context)
    
def delete_from_cart(request, book_id):
    book = get_object_or_404(Cart, id=book_id)
    book.delete()
    return redirect('clients:cart')


        