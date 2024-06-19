from django import forms
from users.models import User, Seller, Client
from sellers.models import Book, BookCategory, BookGenre


class AddSellerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    email = forms.EmailField(widget=forms.TextInput({"class": "form-control", "placeholder": "Email"}))

    password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput({"class": "form-control", "placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return password

class BookCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)

    class Meta:
        model = BookCategory
        fields = ['name', 'description', 'image']

class BookGenreForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    
    class Meta:
        model = BookGenre
        fields = ['name', 'description', 'image']

class EditSellerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Name"}))
    first_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Last Name"}))
    email = forms.EmailField(widget=forms.TextInput({"class": "form-control", "placeholder": "Email"}))
    phone_number = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Phone Number"}))
    image = forms.ImageField(widget=forms.FileInput({"class": "form-control", "placeholder": "Image"}))
    address = forms.CharField(widget=forms.TextInput({"class": "form-control", "placeholder": "Address"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'image', 'address', 'user_role')