from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import BookForm
from .models import Book, BookCategory, BookGenre
from users.permissions import SellerRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class AddBookView(SellerRequiredMixin, View):
    def get(self, request):
        form = BookForm()
        return render(request, 'sellers/add_book.html', {'form': form})
    
    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.seller = request.user
            book.save()
            return redirect('sellers:my_books')
        return render(request, 'sellers/add_book.html', {'form': form})

class EditBookView(SellerRequiredMixin, View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = BookForm(instance=book)
        return render(request, 'sellers/edit_book.html', {'form': form})
    
    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('sellers:my_books')
        return render(request, 'sellers/edit_book.html', {'form': form})
    
class DeleteBookView(SellerRequiredMixin, View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.delete()
        return redirect('sellers:my_books')
    
class MyBooksView(SellerRequiredMixin, View):
    def get(self, request):
        books = Book.objects.filter(seller=request.user)
        paginator = Paginator(books, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'books': page_obj,
            'page_obj': page_obj,
        }
        return render(request, 'sellers/my_books.html', context=context)
    
