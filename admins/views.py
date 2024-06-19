from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from sellers.models import BookCategory, BookGenre
from users.permissions import AdminRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookCategoryForm, BookGenreForm, AddSellerForm, EditSellerForm
from users.models import Seller, Client, User

# Book Category 
class BookCategoriesView(AdminRequiredMixin, View):
    def get(self, request):
        categories = BookCategory.objects.all()
        return render(request,'admins/book_categories.html', {'categories': categories})
    
class AddBookCategoryView(AdminRequiredMixin, View):
    def get(self, request):
        form = BookCategoryForm()
        return render(request, 'admins/add_book_category.html', {'form': form})
    
    def post(self, request):
        form = BookCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins:book_categories')
        return render(request, 'admins/add_book_category.html', {'form': form})
    
class EditBookCategoryView(AdminRequiredMixin, View):
    def get(self, request, category_id):
        category = get_object_or_404(BookCategory, id=category_id)
        form = BookCategoryForm(instance=category)
        return render(request, 'admins/edit_book_category.html', {'form': form})
    
    def post(self, request, category_id):
        category = get_object_or_404(BookCategory, id=category_id)
        form = BookCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admins:book_categories')
        return render(request, 'admins/edit_book_category.html', {'form': form})
    
class DeleteBookCategoryView(AdminRequiredMixin, View):
    def get(self, request, category_id):
        category = get_object_or_404(BookCategory, id=category_id)
        category.delete()
        return redirect('admins:book_categories')
    
#  Book Genre 
class BookGenresView(AdminRequiredMixin, View):
    def get(self, request):
        genres = BookGenre.objects.all()
        return render(request,'admins/book_genres.html', {'genres': genres})
    
class AddBookGenreView(AdminRequiredMixin, View):
    def get(self, request):
        form = BookGenreForm()
        return render(request, 'admins/add_book_genre.html', {'form': form})
    
    def post(self, request):
        form = BookGenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admins:book_genres')
        return render(request, 'admins/add_book_genre.html', {'form': form})
    
class EditBookGenreView(AdminRequiredMixin, View):
    def get(self, request, genre_id):
        genre = get_object_or_404(BookGenre, id=genre_id)
        form = BookGenreForm(instance=genre)
        return render(request, 'admins/edit_book_genre.html', {'form': form})
    
    def post(self, request, genre_id):
        genre = get_object_or_404(BookGenre, id=genre_id)
        form = BookGenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('admins:book_genres')
        return render(request, 'admins/edit_book_genre.html', {'form': form})
    
class DeleteBookGenreView(AdminRequiredMixin, View):
    def get(self, request, genre_id):
        genre = get_object_or_404(BookGenre, id=genre_id)
        genre.delete()
        return redirect('admins:book_genres')
    
# Sellers 
class SellersView(AdminRequiredMixin, View):
    def get(self, request):
        sellers = User.objects.filter(user_role='seller')
        return render(request,'admins/sellers.html', {'sellers': sellers})
    
class AddSellerView(AdminRequiredMixin, View):
    def get(self, request):
        form = AddSellerForm()
        return render(request, 'admins/add_seller.html', {'form': form})
    
    def post(self, request):
        form = AddSellerForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.user_role = 'seller' 
            password = form.cleaned_data['password']
            user.set_password(password) 
            user.save()  
            seller = Seller(user=user)
            seller.save() 
            return redirect('admins:sellers_list')
        return render(request, 'admins/add_seller.html', {'form': form})
    
class EditSellerView(AdminRequiredMixin, View):
    def get(self, request, seller_id):
        seller = get_object_or_404(User, id=seller_id)
        form = EditSellerForm(instance=seller)
        return render(request, 'admins/edit_seller.html', {'form': form})
    
    def post(self, request, seller_id):
        seller = get_object_or_404(User, id=seller_id)
        form = EditSellerForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()
            return redirect('admins:sellers_list')
        return render(request, 'admins/edit_seller.html', {'form': form})
    
class DeleteSellerView(AdminRequiredMixin, View):
    def get(self, request, seller_id):
        seller = get_object_or_404(User, id=seller_id)
        seller.delete()
        return redirect('admins:sellers_list')
    

# Clients

class ClientsView(AdminRequiredMixin, View):
    def get(self, request):
        clients = User.objects.filter(user_role='client')
        return render(request,'admins/clients.html', {'clients': clients})
    
class DeleteClientView(AdminRequiredMixin, View):
    def get(self, request, client_id):
        client = get_object_or_404(User, id=client_id)
        client.delete()
        return redirect('admins:clients_list')
    
class EditClientView(AdminRequiredMixin, View):
    def get(self, request, client_id):
        client = get_object_or_404(User, id=client_id)
        form = EditSellerForm(instance=client)
        return render(request, 'admins/edit_client.html', {'form': form})
    
    def post(self, request, client_id):
        client = get_object_or_404(User, id=client_id)
        form = EditSellerForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('admins:clients_list')
        return render(request, 'admins/edit_client.html', {'form': form})
    