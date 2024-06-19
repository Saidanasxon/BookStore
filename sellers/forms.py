from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Title"}))
    author = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Author"}))
    price = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Price"}))
    description = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Description"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "Image"}))
    quantity = forms.IntegerField(widget=forms.NumberInput({"class": "form-control", "placeholder": "Quantity"}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'quantity', 'price', 'image', 'genre', 'category', 'is_bestseller', 'in_stock']