from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, RegisterForm, EditProfileForm
from .models import User, Client, Seller
from .permissions import AdminRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from sellers.models import Book, BookCategory, BookGenre
from clients.models import Cart

class IndexView(View):
    def get(self, request):
        books = Book.objects.all()
        categories = BookCategory.objects.all()
        genres = BookGenre.objects.all()
        bestsellers = Book.objects.filter(is_bestseller=True)
        
        context = {
            'books': books,
            'categories': categories,
            'genres': genres,
            'bestsellers': bestsellers,
        }
        return render(request, 'users/index.html', context=context)

def about(request):
    return render(request, 'users/about.html')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            print(form.errors)

        return render(request, 'users/login.html', {'form': form})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'client':
                new_client = Client()
                new_client.user = user
                new_client.save()
                
            elif user.user_role == 'seller':
                new_seller = Seller()
                new_seller.user = user
                new_seller.save()

            return redirect('/')
        else:
            print(form.errors)

        form = RegisterForm()
        return render(request, 'users/login.html', {'form': form})
    

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditProfileForm(instance=request.user)
        return render(request, 'users/profile.html', {'form': form})
    
    def post(self, request):
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
        elif form.errors:
            form.user_role = 'client'
            if form.is_valid():
                form.save()
                return redirect('users:profile')
        
        form = EditProfileForm(instance=request.user)
        return render(request, 'users/profile.html', {'form': form})