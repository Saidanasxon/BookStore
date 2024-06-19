from django.contrib import admin
from .models import Book, BookCategory, BookGenre

admin.site.register(Book)

admin.site.register(BookCategory)

admin.site.register(BookGenre)